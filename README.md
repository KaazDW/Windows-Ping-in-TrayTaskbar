# Windows-Ping-Taskbar-Widget

Display your real-time ping directly in the Windows system tray with this lightweight Python widget.

<p align="center">
    <img src="https://github.com/KaazDW/ping.py/blob/main/screen_taskbar.png" width="500"/>
</p>

## Features

- **Real-time ping display in the Windows system tray**
- Context menu (right-click) with options:
  - **Open Github**: Opens the project page
  - **Quit**: Closes the widget
- Automatic startup with Windows (see below)

## Installation

1. **Clone the repository or download the files**
2. **Install Python dependencies**:

   ```shell
   pip install pystray pillow ping3
   ```

3. **Automate startup with Windows**  
   Use the provided batch script to copy the script to `%appdata%` and create a startup shortcut:

   - Double-click `automated-startup.bat`
   - The widget will launch automatically at every Windows startup

## Usage

- Run `taskbar.py` (or let the batch script handle it at startup)
- The ping will be displayed in the system tray
- Right-click the icon to access the menu (GitHub, Quit)

## Uninstallation
- execute uninstall.bat
or
- Delete the `%appdata%\PingTaskbarWidget` folder
- Delete the `PingTaskbarWidget.lnk` shortcut from the Startup folder (`shell:startup`)

## Notes

- The script uses `pythonw.exe` to avoid opening a console window.  
  Make sure Python is installed and available in your PATH.
- For questions or suggestions, open an issue or pull request!

---

⭐ Feel free to star and share this project if you like it!