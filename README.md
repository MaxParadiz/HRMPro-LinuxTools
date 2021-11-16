Very simple, minimal script that allows you to print the heart rate measured by Garmin's HRM-Pro strap.

Replace the MAC address with the address of your HRM-Pro strap. 

To find the mac address, run bluetoothctl and 

Run this in the terminal as sudo python HeartRate.py (sudo needed for establishing bluetooth connection) and your measured heart rate will be printed every second.
