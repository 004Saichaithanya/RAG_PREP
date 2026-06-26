from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("calculator")


@mcp.tool()
def as_number(value: str) -> float:
    """
    Convert a string to a number.
    Example: "10.5" -> 10.5
    """
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"'{value}' is not a valid number.")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide the first number by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.tool()
def power(a: float, b: float) -> float:
    """Raise a to the power of b."""
    return a ** b


@mcp.tool()
def modulo(a: float, b: float) -> float:
    """Return the remainder after division."""
    return a % b


@mcp.tool()
def sqrt(x: float) -> float:
    """Return the square root."""
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return x ** 0.5


@mcp.tool()
def absolute(x: float) -> float:
    """Return the absolute value."""
    return abs(x)

if __name__ == "__main__":
    print("running..")
    mcp.run()