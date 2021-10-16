import paho.mqtt.client as mqtt

DATACAKE_TOKEN = "yourdatacaketokenhere"

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

if __name__ == "__main__":

    client.on_connect = on_connect
    client.on_message = on_message

    client.tls_set()
    client.username_pw_set(DATACAKE_TOKEN, password=DATACAKE_TOKEN)
    client.connect("mqtt.datacake.co", 8883, 60)
    client.loop_start()

    # random data
    number_of_persons_a = 234
    number_of_persons_b = 345

    # publish to Datacake Device
    client.publish(
        "dtck-pub/luxonis-device-product/aa8d19b8-4cfc-40bc-801d-5212e82b4c4f/NUMBER_OF_PERSONS_A",
        number_of_persons_a
    )

    client.publish(
        "dtck-pub/luxonis-device-product/aa8d19b8-4cfc-40bc-801d-5212e82b4c4f/NUMBER_OF_PERSONS_B",
        number_of_persons_b
    )
