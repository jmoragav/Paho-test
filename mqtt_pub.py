import paho.mqtt.client as paho
import sys

import json
 
MQTT_HOST = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "iris"

MQTT_MSG=json.dumps({"sepalLength": "6.4","sepalWidth":  "3.2","petalLength": "4.5","petalWidth":  "1.5"}) 
 
def on_publish(client, userdata, mid):
    print("Mensaje Publicado")

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC)
    client.publish(MQTT_TOPIC, MQTT_MSG)

def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload)  
    payload = json.loads(msg.payload)  
    print(payload['sepalWidth'])  
    client.disconnect()  

 
mqttc = paho.Client()

 
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect
mqttc.on_message = on_message
 

if mqttc.connect(MQTT_HOST,MQTT_PORT,MQTT_KEEPALIVE_INTERVAL) != 0:
    print("No se pudo conectar con el broker")
    sys.exit(-1)

# Loop forever
mqttc.loop_forever()

 

 