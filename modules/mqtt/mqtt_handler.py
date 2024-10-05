import paho.mqtt.client as mqtt
from settings import BROKER_ADDRESS, BROKER_PORT, TOPIC


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connexion réussie au broker MQTT")
        client.subscribe(TOPIC)
    else:
        print(f"Échec de la connexion. Code de retour = {rc}")


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(f"Déconnexion inattendue. Code de retour = {rc}")
    else:
        print("Déconnexion propre du broker MQTT")


def on_message(client, userdata, msg):
    print(f"Message reçu sur {msg.topic}: {msg.payload.decode()}")


def on_publish(client, userdata, mid):
    print(f"Message publié avec ID {mid}")


def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Abonnement au topic avec ID {mid} et QoS {granted_qos}")


def run():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_publish = on_publish
    client.on_subscribe = on_subscribe

    try:
        client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
    except Exception as e:
        print(f"Erreur de connexion au broker MQTT: {e}")
        return

    try:
        client.loop_start()
    except KeyboardInterrupt:
        print("Orvouar")

    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    run()
