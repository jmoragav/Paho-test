
import paho.mqtt.client as paho
import sys



 
MQTT_HOST = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "iris"


def onMessage(client,userdata,msg):
    print(msg.topic+ ": " + msg.payload.decode())

client= paho.Client()
client.on_message=onMessage


if client.connect(MQTT_HOST,MQTT_PORT,MQTT_KEEPALIVE_INTERVAL) != 0:
    print("No se pudo conectar con el broker")
    sys.exit(-1)


client.subscribe(MQTT_TOPIC)



try:
    print("Ctrl+C para parar")
    client.loop_forever()

except:
    print("Desconectado")

client.disconnect()