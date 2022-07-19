#!/usr/local/bin/python3
from lib2to3.pgen2.token import PERCENT
import psutil, os

kill_percent = 5

pointer = []
for process in psutil.process_iter():
    # Get the Logitech Presentation PID.
    if process.name() == 'Logitech Presentation':
        pointer.append(process)

for pid in pointer:
    for _ in range(1):
        # check memory usage over kill_percent (variable above) physical memory
        if pid.memory_percent() < kill_percent or not pid.is_running():
#            print("the pid is:", pid.pid ,"and the pid memory is:", pid.memory_percent(), "and the kill_percent is:", kill_percent )
             # no action, spotlight is using less than kill_percent (variable above) of memory or process isn't running
#            print("There is no action necessary, memory utiliztion is", round(pid.memory_percent(),2),"%")
            break
    else:
        # spotlight is using more than kill_percent (variable above) of physical memory and will be killed/restarted
        pid.kill()
#        print("The process is using far too much memory, KILL IT, utiliztion is", round(pid.memory_percent(),2),"%")
        # Execute LogiPresentation 
        os.system("/Library/Application\ Support/Logitech.localized/Logitech\ Presentation.localized/Logitech\ Presentation.app/Contents/MacOS/Logitech\ Presentation &")
