# Welcome to your Expo app 👋

This is an [Expo](https://expo.dev) project created with [`create-expo-app`](https://www.npmjs.com/package/create-expo-app).

## Get started

1. Install dependencies

   ```bash
   npm install
   ```

2. Start the app

   ```bash
   npx expo start
   ```

In the output, you'll find options to open the app in a

- [development build](https://docs.expo.dev/develop/development-builds/introduction/)
- [Android emulator](https://docs.expo.dev/workflow/android-studio-emulator/)
- [iOS simulator](https://docs.expo.dev/workflow/ios-simulator/)
- [Expo Go](https://expo.dev/go), a limited sandbox for trying out app development with Expo

You can start developing by editing the files inside the **app** directory. This project uses [file-based routing](https://docs.expo.dev/router/introduction).

## Get a fresh project

When you're ready, run:

```bash
npm run reset-project
```

This command will move the starter code to the **app-example** directory and create a blank **app** directory where you can start developing.

## Learn more

To learn more about developing your project with Expo, look at the following resources:

- [Expo documentation](https://docs.expo.dev/): Learn fundamentals, or go into advanced topics with our [guides](https://docs.expo.dev/guides).
- [Learn Expo tutorial](https://docs.expo.dev/tutorial/introduction/): Follow a step-by-step tutorial where you'll create a project that runs on Android, iOS, and the web.

## Join the community

Join our community of developers creating universal apps.

- [Expo on GitHub](https://github.com/expo/expo): View our open source platform and contribute.
- [Discord community](https://chat.expo.dev): Chat with Expo users and ask questions.




# Windows Build commands using Android SDK and Home 

# `panel-installer` – Run on Android Phone (Windows Setup)

## Prerequisites

Install these first:

* Node.js
* Android Studio
* Expo CLI
* USB cable
* Android phone with Developer Options enabled

---

# 1. Clone / open project

Open **Command Prompt / PowerShell**

Go to project:

```bash
cd C:\SaiChaithanya\Radionix\panel-installer
```

---

# 2. Install node modules

Run:

```bash
npm install
```

or

```bash
npm i
```

---

# 3. Verify Android SDK installed

Open Android Studio:

**Settings → Android SDK**

Copy SDK path.

Usually:

```txt
C:\Users\SaiChaithanya\AppData\Local\Android\Sdk
```

Inside SDK folder verify:

```txt
platform-tools
platforms
build-tools
emulator
cmdline-tools
```

---

# 4. Add Android environment variables

## Open environment variables

Windows Search:

```txt
Edit the system environment variables
```

Open:

```txt
Advanced → Environment Variables
```

---

## Add ANDROID_HOME

User variables → **New**

Name:

```txt
ANDROID_HOME
```

Value:

```txt
C:\Users\SaiChaithanya\AppData\Local\Android\Sdk
```

---

## Add ANDROID_SDK_ROOT

User variables → **New**

Name:

```txt
ANDROID_SDK_ROOT
```

Value:

```txt
C:\Users\SaiChaithanya\AppData\Local\Android\Sdk
```

---

## Add PATH entries

User variables → Path → Edit → New

Add:

```txt
%ANDROID_HOME%\platform-tools
```

```txt
%ANDROID_HOME%\emulator
```

```txt
%ANDROID_HOME%\cmdline-tools\latest\bin
```

Click **OK**

Restart terminal.

---

# 5. Verify adb

Open new CMD:

Check:

```bash
adb version
```

Check location:

```bash
where adb
```

Expected:

```txt
C:\Users\SaiChaithanya\AppData\Local\Android\Sdk\platform-tools\adb.exe
```

---

# 6. Enable developer options on phone

On Android phone:

Settings → About phone

Tap:

```txt
Build Number
```

7 times

Developer options enabled.

---

# 7. Enable USB debugging

Phone:

Settings → Developer Options

Enable:

✅ USB Debugging

Optional:

✅ Install via USB

✅ USB debugging (Security settings)

---

# 8. Connect phone with USB

Connect device.

Phone popup:

```txt
Allow USB debugging?
```

Tap:

```txt
Allow
```

---

# 9. Verify device from PC

Run:

```bash
adb devices
```

Example:

```txt
List of devices attached
abcd12345    device
```

If unauthorized:

```bash
adb kill-server
adb start-server
adb devices
```

Allow popup on phone again.

---

# 10. Create Android local.properties

Go to:

```txt
C:\SaiChaithanya\Radionix\panel-installer\android
```

Create file:

```txt
local.properties
```

Add:

```properties
sdk.dir=C:\\Users\\SaiChaithanya\\AppData\\Local\\Android\\Sdk
```

Save.

---

# 11. Clear old build (optional)

Inside project:

```bash
cd android
gradlew clean
cd ..
```

---

# 12. Start Expo

Project root:

```bash
npx expo start
```

or directly build Android:

```bash
npx expo run:android
```

---

# 13. If Metro already needed

Run:

```bash
npx expo start --clear
```

---

# 14. Common adb commands

Check device:

```bash
adb devices
```

Restart adb:

```bash
adb kill-server
adb start-server
```

Install apk manually:

```bash
adb install app-debug.apk
```

Reverse Metro port:

```bash
adb reverse tcp:8081 tcp:8081
```

Logs:

```bash
adb logcat
```

---

# 15. Common issues

## SDK location not found

Fix:

```txt
android/local.properties
```

Add:

```properties
sdk.dir=C:\\Users\\SaiChaithanya\\AppData\\Local\\Android\\Sdk
```

---

## adb not recognized

Check PATH

Run:

```bash
where adb
```

---

## Device unauthorized

Run:

```bash
adb kill-server
adb start-server
adb devices
```

Accept popup on phone.

---

## Metro cache issues

Run:

```bash
npx expo start --clear
```

---

## Gradle clean

```bash
cd android
gradlew clean
cd ..
```

---

# Final run

Most common workflow:

```bash
cd C:\SaiChaithanya\Radionix\panel-installer
npm install
adb devices
npx expo run:android
```

After first build:

```bash
npx expo start
```

Then app runs on your Android phone over USB.


---

# Project Architecture & Recent Updates

We recently refactored the application navigation flow, resolved layout routing conflicts, implemented the **Add Output** feature, and integrated the **Users** tab stack.

## 📂 File Structure & Newly Added/Modified Files

Below is the updated file structure of the navigation, device dashboard, output, and user management modules:

```txt
src/
├── api/
│   ├── output.ts                 # API client for singular output calls
│   └── outputs.ts                # API client for batch outputs calls
├── app/
│   ├── +not-found.tsx            # Fallback error screen
│   ├── _layout.tsx               # Root Stack Navigator configuration (registers Select Site stack & Panels layout)
│   ├── index.tsx                 # App entry route directly exporting SelectSiteScreen
│   └── panels/
│       └── [id]/
│           ├── _layout.tsx       # Bottom tabs navigation scoped to dynamic Panel ID (Devices, Scan, Home, Users)
│           ├── index.tsx                 # Panel Devices Dashboard (renders DevicesScreen)
│           ├── scan.tsx          # Panel Scan tab mapping
│           ├── home.tsx          # Panel diagnostics and mock counter home screen
│           ├── add_output.tsx    # Re-export route for AddOutputScreen
│           └── users/
│               ├── _layout.tsx   # Stack layout for Users tab (List, Create, Roles)
│               ├── index.tsx     # List of site users
│               ├── add-user.tsx  # Add new user route
│               └── [roleId].tsx  # User role details route
├── hooks/
│   ├── output/
│   │   └── useCreateOutput.ts    # React Query useMutation hook for adding outputs (singular)
│   └── outputs/
│       └── useCreateOutput.ts    # Re-exports output hook for backwards compatibility (plural)
├── schemas/
│   └── outputSchema.ts           # Strict Zod schema for OutputCreate request validation
├── screens/
│   ├── devicedashboard/
│   │   └── AddOutputScreen.tsx   # Form screen to create physical or virtual outputs
│   └── DevicesScreen/
│       ├── DeviceDashboardScreen.tsx # High-density Devices view (Points and Outputs tabs, connected FAB)
│       └── components/
│           ├── AddDeviceFAB.tsx  # FAB floating button triggering actions
│           └── OutputItem.tsx    # Renders single output card details
```

---

## 🛠️ Working and Summary of Recent Changes

### Outputs Page & "Add Output" Feature
We implemented the **Add Output** feature to allow technicians to create new physical or virtual outputs for a panel:
* **API Integration**: Created `GET /panels/${panelId}/outputs` and `POST /panels/${panelId}/outputs` calls inside [`src/api/output.ts`](file:///c:/SaiChaithanya/Radionix/panel-installer/src/api/output.ts) and [`src/api/outputs.ts`](file:///c:/SaiChaithanya/Radionix/panel-installer/src/api/outputs.ts) using the shared Axios instance.
* **Zod Validation**: Defined `createOutputSchema` in [`src/schemas/outputSchema.ts`](file:///c:/SaiChaithanya/Radionix/panel-installer/src/schemas/outputSchema.ts) enforcing non-control characters on names, profile range (1-20), output states, and user control toggle parameters.
* **React Query mutation**: Implemented `useCreateOutput` mutation hook under [`src/hooks/output/useCreateOutput.ts`](file:///c:/SaiChaithanya/Radionix/panel-installer/src/hooks/output/useCreateOutput.ts) to handle POST submission, auto-invalidate client query caches, show feedback alerts, and execute page rollback navigation.
* **Interactive Form Screen**: Created [`AddOutputScreen.tsx`](file:///c:/SaiChaithanya/Radionix/panel-installer/src/screens/devicedashboard/AddOutputScreen.tsx) using `react-hook-form` controllers, custom BottomSheet option selection wrappers, active Switches, and NativeWind styling.
* **Dashboard FAB Action**: Hooked up the Add Device button inside the [`DeviceDashboardScreen.tsx`](file:///c:/SaiChaithanya/Radionix/panel-installer/src/screens/DevicesScreen/DeviceDashboardScreen.tsx) to redirect to the new Add Output screen when the Outputs tab is selected.
