#!/usr/local/bin/python3
import psutil, os

kill_percent = 5
pointer = []

for process in psutil.process_iter():
    # Get the Logitech Presentation PID.
    if process.name() == 'Logitech Presentation':
        pointer.append(process)

for pid in pointer:
    for _ in range(1):
        if pid.memory_percent() < kill_percent or not pid.is_running():
#            print("PID:", pid.pid,"| Memory:", round(pid.memory_percent(),2), "% | kill_percent:", kill_percent, "%" )
            break
    else:
        pid.kill()
#        print("The process is using far too much memory, KILL IT, utiliztion is", round(pid.memory_percent(),2),"%")
        os.system("/Library/Application\ Support/Logitech.localized/Logitech\ Presentation.localized/Logitech\ Presentation.app/Contents/MacOS/Logitech\ Presentation &")
