# spotlight-monitor
A quick script to monitor the Logitech Spotlight's memory leak &amp; restart the daemon. Tested on Mac (12.4), though it probably works on Linux too. 

This is a simple python script. You can simply execute the script when needed to do a quick restart of the daemon. I have choosen to use a cron job to periodically check the memory usage and restart when crossing a threashhold (variable in script). The Spotlight reconnects in ~1 second so I haven't found this to be disruptive even in the middle of a presentation. Nothing shows on your extended screen (assuming two displays) but you will see the restart as the process reloads on your main display...still not nearly as disruptive as the pointer making your entire computer unresponsive as it consumes all system memory. 

# ![permissions](https://github.com/brian-olson/spotlight-monitor/blob/main/images/restart.png)

In order to make this work with cron on OS X you will need to grant cron some permissions. I simply went through the "Security & Privacy" preferences and added cron to all categories Spotlight was enabled. Those were: 

- Accessibility 
- Input Monitoring
- Screen Recording
- Bluetooth

![permissions](https://github.com/brian-olson/spotlight-monitor/blob/main/images/privs.png)

In order to add cron Open "Security & Privacy," then unlock the interface. On the sections above, click the plus to add a new entry. A finder window will then appear however most of the file system is hidden. To unhide them press the “Command” + “Shift” + “.” (period) keys at the same time. Then you can browse to "$username's Macbook Pro" (the root HDD) and you'll find cron in /usr/sbin/. 

Once permissions are granted you are ready to setup crontab. The command below will open crontab in VIM. 

`crontab -e`

Then you'll want to add a command something like this: 

`*/10 * * * * /usr/local/bin/python3 ~/spotlight_mem.py`

![crontab](https://github.com/brian-olson/spotlight-monitor/blob/main/images/crontab.png)

Be sure to update the location to python as well as the script file. You can find you python installation with `which python`. This entry will run the script every 10 minutes (you may wish to change this). 

NOTE: This is how I made it work. This might not be the most secure configuration (giving cron blanket privs). 