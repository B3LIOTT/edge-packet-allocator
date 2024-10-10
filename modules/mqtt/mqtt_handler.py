import paho.mqtt.client as mqtt
from settings import *
from time import sleep


class WorkersStats:
    stats = {}
    waiting_stats = False

    @staticmethod
    def get_stats():
        if TEST_MODE:
            print("Getting stats from workers...")

        WorkersStats.waiting_stats = True
        # ping_workers(client)

        # dummy
        sleep(0.5)
        WorkersStats.stats = {
            'packet_worker_1': (10, 1024 * 1),
            'packet_worker_2': (80, 1024 * 10),
            'packet_worker_3': (20, 1024 * 1000)
        }
        WorkersStats.waiting_stats = False
        # -----

        # wait for responses from workers
        timeout = 50  # if it takes more than 50*0.1 = 5 seconds, then we raise an alert
        while WorkersStats.waiting_stats:
            if timeout == 0:
                print("Timeout: Workers did not respond")
                break

            sleep(0.1)
            timeout -= 1

        if TEST_MODE:
            print("Stats received")


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connexion réussie au broker MQTT")
        client.subscribe(WORKERS_STATS)
    else:
        print(f"Échec de la connexion. Code de retour = {rc}")


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(f"Déconnexion inattendue. Code de retour = {rc}")
    else:
        print("Déconnexion propre du broker MQTT")


def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"Message reçu sur {msg.topic}: {payload}")

    # parse stats
    # je dois recevoir le topic sur lequel le worker attend les packets, le cpu load et la mémoire restante
    WorkersStats.stats[msg.topic] = msg.payload.decode().split(',')

    if len(WorkersStats.stats) == N_WORKERS:
        WorkersStats.waiting_stats = False


def on_publish(client, userdata, mid):
    print(f"Message publié avec ID {mid}")


def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Abonnement au topic avec ID {mid} et QoS {granted_qos}")


def ping_workers(client):
    for topic in WORKERS_PING:
        client.publish(topic, PING_MSG)


def connect():
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
        dispose(client)
        exit(1)

    client.loop_start()

    return client


def dispose(client):
    client.loop_stop()
    client.disconnect()


if __name__ == "__main__":
    print(connect())
