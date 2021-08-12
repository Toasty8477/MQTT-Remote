# MQTT-Remote

A simple MQTT controller for Home Assistant.  

## Reqirements

- An ESP8266 breakout board. I'm using a Wemos D1 clone.
- A device running an mqtt broker like [Mosquitto](https://mosquitto.org/).
- A Micropython compatible IDE. I'm using [Thonny](https://thonny.org/).

## How to flash MicroPython

To run this program you will need to flsh micropython to your esp8266. You will need the [ESPHome Flasher](https://github.com/esphome/esphome-flasher/tree/master) and the latest [Micropython Firmware](https://micropython.org/download/esp8266/).

To install the firmware first plug your device into a usb port on your computer and open the esphome flasher. Choose what COM port to use (check device manager if you are unsure) and choose the firmware file you just downloaded. Now select flash ESP and wait for the flasher to finish.

## Uploading the Code

First you will need to download the main.py and ConnectWifi.py files. Once downloaded open the files in thonny.  
You will first need to edit ConnectWifi.py and add your network ssid and passphrase.  
Once you have done this go to file in the top right corner and select save as. When asked where to save to select micropython device. Make sure to name the files the same as the originals. Do this for both files.

## Buliding the Controller
This project is not finished and will be updated as it improves for now you can build the example schematic.  
#### The example reqires:
- 1x ESP8266
- 1x Linea potentiometer
- 3x SPST Momentary switches or buttons
- 3x 10k Ω resistors
- 1x Solderless breadboard
