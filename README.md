# ping.py
 
 

<p align="center">
<span>Python script allow you to **show your ping info** in real time on your screen like a widget, or in taskbar.</span>
    <br/><br/>
    <img src="https://github.com/KaazDW/ping.py/blob/main/screen_taskbar.png" width="500"/>
    <img src="https://github.com/KaazDW/ping.py/blob/main/screen_window.png" width="500"/>
</p>

## Installation

Clone the repository or download the script file.
Install the required Python libraries:

for ```window.py```
```
pip install psutil ping3
```

for ```taskbar.py```
```
pip install pystray pillow ping3
```

## Windows Auto-Start

1. Press ```Win+R```, type ```shell:startup```, and press ```Enter```.
2. Copy the ```.bat``` file to this folder.
3. Rename it as you want, maybe something like ```Ping Taskbar Display```
4. Change the source link in the ```.bat``` 
   
On the next reboot, the script will be executed automatically, and be display in the ```Task Manager``` 'Auto Start App' tab.
