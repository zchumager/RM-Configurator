**BROADLINK RM CONFIGURATOR**

IT IS REALLY IMPORTANT EXECUTE PIP FREEZE ON TXT FILE TO DOWNLOAD DEPENDENCIES

pip3 freeze -r requirements.txt

Python CLI Tool for retrieving network information of any Broadlink device like RM2, RM3 and RM4 IR/RF Hub  
. At present, the following devices are currently supported:  

 - RM Pro (referred to as RM2 in the codebase)
 - A1 sensor platform devices are supported  
 - RM3 mini IR blaster  
 - RM4 and RM4C mini blasters  
 - There is currently no support for the cloud API.

**Put device into AP Mode**  
Setup a new device on your local wireless network:  
 
 1. Long press the reset button until the blue LED is blinking quickly (like 7 seconds).  
 2. Long press again until blue LED is blinking slowly (like 14 seconds).  
 3. Manually connect to the WiFi SSID named BroadlinkProv.
 4. Run rm_config with python3 interpreter
 
> python3 src/rm_config.py --sssid SSID_2.4 --password SSID_PASSWORD --mode  NETWORK_MODE

Mode (0 = none, 1 = WEP, 2 = WPA1, 3 = WPA2, 4 = WPA1/2)

Once the RM Config is already configured just run the CLI with --details flag to get all RM Mini Connection Data
> python3 src/rm_config.py --details

Also as addition --getip is included to get a free IP address to used as static
> python3 src/rm_config.py --getip

for further information use the help flag

> python3 src/rm_config.py --help
