import RPi.GPIO as GPIO		#import RPi.GPIO module
import requests
import json
import collections
import time

def create_object(self):
    return collections.namedtuple('object_name', keys)(* values)

prev_input = 1
counter = 0
LED = 16			#pin no. as per BOARD, GPIO18 as per BCM
Switch_input = 18		#pin no. as per BOARD, GPIO27 as per BCM
GPIO.setwarnings(False) 	#disable warnings
GPIO.setmode(GPIO.BOARD)	#set pin numbering format
GPIO.setup(LED, GPIO.OUT)	#set GPIO as output
GPIO.setup(Switch_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)
starttime = time.time()
x = requests.post('https://raspberry3.herokuapp.com/user/user',data ={'username':'محمد'})
a_json = x.text
a_dict_json = json.loads(a_json)
keys = a_dict_json.keys()
values = a_dict_json.values()
an_object = json.loads(a_json, object_hook=create_object)
if(an_object.status=='واصل'):
    GPIO.output(LED,GPIO.HIGH)
else:
    GPIO.output(LED,GPIO.LOW)
while True:
    input = GPIO.input(Switch_input)
    if ((not prev_input) and (input)):
        print("Button pressed")
        counter=counter+1
    prev_input = input
    time.sleep(0.05)
    print(time.time() - starttime)
    if(time.time() - starttime>30):
        print ("send")
        x = requests.post('https://raspberry3.herokuapp.com/user/newConsumption',data ={'username':'محمد','counter':counter})
        x = requests.post('https://raspberry3.herokuapp.com/user/user',data ={'username':'محمد'})
        a_json = x.text
        a_dict_json = json.loads(a_json)
        keys = a_dict_json.keys()
        values = a_dict_json.values()
        an_object = json.loads(a_json, object_hook=create_object)
        if(an_object.status=='واصل'):
            GPIO.output(LED,GPIO.HIGH)
        else:
            GPIO.output(LED,GPIO.LOW)
        counter = 0    
        starttime=time.time();
    print(counter)
