import paho.mqtt.client as mqtt
from settings import *
from time import sleep


stats = {}


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

    # parse stats
    # je dois recevoir le topic sur lequel le worker attend les packets, le cpu load et la mémoire restante
    stats["topic"] = (10, 10)  # msg.payload.decode().split(',')


def on_publish(client, userdata, mid):
    print(f"Message publié avec ID {mid}")


def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Abonnement au topic avec ID {mid} et QoS {granted_qos}")


def ping_workers(client):
    for topic in WORKERS_PING:
        client.publish(topic, PING_MSG)


def run():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_publish = on_publish
    client.on_subscribe = on_subscribe

    # try:
    #     client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
    # except Exception as e:
    #     print(f"Erreur de connexion au broker MQTT: {e}")
    #     return
    #
    # try:
    #     client.loop_start()
    #
    #     # ask wokers for stats
    #     ping_workers(client)
    #
    #     # wait for responses in WORKERS_STATS topics
    #     sleep(1)
    #
    # except KeyboardInterrupt:
    #     print("Orvouar")
    #
    # finally:
    #     client.loop_stop()
    #     client.disconnect()

    stats_test = {
        'edge1-topic': (10, 1024 * 1),
        'edge2-topic': (80, 1024 * 10),
        'edge3-topic': (20, 1024 * 1000)
    }

    return stats_test


if __name__ == "__main__":
    print(run())
