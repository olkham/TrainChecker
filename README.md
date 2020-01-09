# TrainChecker

The script I currently use my home automation system to check train times in the morning.
It's being executed by Node-RED on an RPi the results are then broadcast to multiple Google Home Smart speakers around the house.

To use, create another file api_key.py in which you define the LDB_TOKEN = 'API_TOKEN' that you can obtain from
http://realtime.nationalrail.co.uk/OpenLDBWSRegistration

To use python in Node-RED 
1. Install [node-red-contrib-pythonshell](https://flows.nodered.org/node/node-red-contrib-pythonshell) from the Palette manager.
2. Add the path to the .py file e.g. /home/pi/HomeAutomation/getDepartureBoard.py
3. Add the virtual environment (if used) e.g. /home/pi/.conda/envs/smarthome

The python line sys.stdout.write() puts the JSON reply from NationalRail into msg.payload from the python node
I then use a function node in Node-RED to parse this using...

```
msg.payload = JSON.parse(msg.payload)
```

Then extract the relevant info to you and do something cool with it!
