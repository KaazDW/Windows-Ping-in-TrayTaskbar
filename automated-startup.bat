@echo off
setlocal

REM Var init
set "SRC=%~dp0taskbar.py"
set "APPDIR=%appdata%\PingTaskbarWidget"
set "STARTUP=%appdata%\Microsoft\Windows\Start Menu\Programs\Startup"
set "PYTHON_EXEC=pythonw.exe"

REM Create application directory if it does not exist
if not exist "%APPDIR%" (
    mkdir "%APPDIR%"
)

REM Script cpoy to the application directory
copy /Y "%SRC%" "%APPDIR%\taskbar.py"

REM Build the run .bat script
echo @echo off > "%APPDIR%\run_ping_widget.bat"
echo start "" "%PYTHON_EXEC%" "%APPDIR%\taskbar.py" >> "%APPDIR%\run_ping_widget.bat"

REM Create a shortcut in the Startup folder to the .bat script
set "VBS=%TEMP%\create_shortcut.vbs"
echo Set oWS = WScript.CreateObject("WScript.Shell") > "%VBS%"
echo sLinkFile = "%STARTUP%\PingTaskbarWidget.lnk" >> "%VBS%"
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> "%VBS%"
echo oLink.TargetPath = "%APPDIR%\run_ping_widget.bat" >> "%VBS%"
echo oLink.WorkingDirectory = "%APPDIR%" >> "%VBS%"
echo oLink.Save >> "%VBS%"
cscript //nologo "%VBS%"
del "%VBS%"

echo Installation complete. The Ping Taskbar Widget will start automatically on next login.
pause