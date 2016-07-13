import paho.mqtt.client as mqtt

PublisherAdress = "192.168.0.100"

def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("Messung")
	
		
def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        message = str(msg.payload)
        text_file = open("Output.csv", "a")
        text_file.write(message)
        #text_file.close
        

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(PublisherAdress, 1883, 60)



client.publish(PublisherAdress,"Online")

client.loop_forever()
