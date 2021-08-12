from machine import Pin, ADC
import time
import math
import ConnectWifi
import ubinascii
from umqtt.simple import MQTTClient

ConnectWifi.connect()
print('RUN: main.py')

CLIENT_ID = ubinascii.hexlify(machine.unique_id())
mqtt = MQTTClient(CLIENT_ID, '192.168.0.19')
mqtt.connect()

button1 = Pin(2, Pin.IN, Pin.PULL_UP)
button2 = Pin(0, Pin.IN, Pin.PULL_UP)
pot_button = Pin(16, Pin.IN, Pin.PULL_UP)
adc = ADC(0)

def scale_value(value, in_min, in_max, out_min, out_max):
  scaled_value = (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
  return math.floor(scaled_value)


while True:
    scene1 = button1.value()
    scene2 = button2.value()
    dim = pot_button.value()
    
    if scene1 == 1:
        print('Scene 1')
        mqtt.publish('light/controller/scene'.format(CLIENT_ID).encode(), str('Scene 1').encode())
        time.sleep_ms(500)
        scene1 = 0  
        
    if scene2 == 1:
        print('Scene 2')
        mqtt.publish('light/controller/scene'.format(CLIENT_ID).encode(), str('Scene 2').encode())
        time.sleep_ms(500)
        scene2 = 0

    if dim == 1:
        print('Dim lights')
        mqtt.publish('light/controller/light'.format(CLIENT_ID).encode(), str(scale_value(adc.read(), 0, 1024, 0, 100)).encode())
        time.sleep_ms(500)
        dim = 0
