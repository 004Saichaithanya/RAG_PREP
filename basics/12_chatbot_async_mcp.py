from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage,HumanMessage,SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.graph.message import add_messages 
# import operator
from langgraph.prebuilt import ToolNode,tools_condition
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
import sys

load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash-lite',
)


#state
class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

# mcp client

client = MultiServerMCPClient(
    {
        "arithm":{
            "transport":"stdio",
            "command":sys.executable,
            'args':['C:/SaiChaithanya/RAG/basics/servers/main.py']
        }
    }
)


async def build_graph():
    tools =await client.get_tools()
    #print(tools)

    llm_with_tools = llm.bind_tools(tools)

    #node
    async def chat_node(state:ChatState) -> ChatState:
        """LLM Node that may answer or request a tool call"""
        messages = state['messages']
        response = await llm_with_tools.ainvoke(messages)

        return {'messages':[response]}

    tool_node  = ToolNode(tools)

    #graph structure
    graph = StateGraph(ChatState)
    graph.add_node('chat_node',chat_node)
    graph.add_node('tools',tool_node)

    graph.add_edge(START,'chat_node')
    graph.add_conditional_edges('chat_node',tools_condition)
    graph.add_edge('tools','chat_node')

    chatbot = graph.compile()

    return chatbot


async def main():
    chatbot = await build_graph()

    result  = await chatbot.ainvoke({'messages':HumanMessage(content = 'what is 10/2 ?')})
    print(result["messages"][-1].content)


if __name__ == '__main__':
    asyncio.run(main())