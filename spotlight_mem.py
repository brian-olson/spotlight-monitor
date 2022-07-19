#!/usr/local/bin/python3
from lib2to3.pgen2.token import PERCENT
import psutil, os

pointer = []
for process in psutil.process_iter():
    # Get the Logitech Presentation PID.
    if process.name() == 'Logitech Presentation':
        print("The Logitech Presentation process is", process.pid)
        pointer.append(process)

for pid in pointer:
    for _ in range(100):
        # check memory usage over 5% physical memory
        if pid.memory_percent() < 5 or not pid.is_running():
            # no action, spotlight is using less than 10% of memory or process isn't running
            print("There is no action necessary, memory utiliztion is", round(pid.memory_percent(),2),"%")
            break
    else:
        # spotlight is using more than 10% of physical memory and will be killed/restarted
        pid.kill()
        print("The process is using far too much memory, KILL IT, utiliztion is", round(pid.memory_percent(),2),"%")
        # Execute LogiPresentation 
        os.system("/Library/Application\ Support/Logitech.localized/Logitech\ Presentation.localized/Logitech\ Presentation.app/Contents/MacOS/Logitech\ Presentation &")
