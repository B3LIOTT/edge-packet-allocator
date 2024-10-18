import paho.mqtt.client as mqtt
from random import randint
from settings import *
from time import sleep
from log_conf import logger


class WorkersStats:
    stats = {}
    waiting_stats = False

    @staticmethod
    def get_stats(client):
        logger.info("Getting stats from workers...")

        WorkersStats.waiting_stats = True
        ping_workers(client)

        # dummy --------------------------------
        # sleep(0.5)
        # WorkersStats.set_stats_value("worker-1" ,(randint(0, 100), MAX_STORAGE))
        # WorkersStats.set_stats_value("worker-2" ,(randint(0, 100), MAX_STORAGE))
        # WorkersStats.set_stats_value("worker-3" ,(randint(0, 100), MAX_STORAGE))
        # WorkersStats.done()
        # --------------------------------------

        # wait for responses from workers
        timeout = 50  # if it takes more than 50*0.1 = 5 seconds, then we raise an alert
        while WorkersStats.waiting_stats:
            if timeout == 0:
                logger.error("Timeout: Workers did not respond")
                break

            sleep(0.1)
            timeout -= 1

    @staticmethod
    def set_stats_value(k, v):
        WorkersStats.stats[k] = v
        logger.info(f"Nouvelles stats : {WorkersStats.stats}")

    @staticmethod
    def done():
        WorkersStats.waiting_stats = False


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info("Connexion réussie au broker MQTT")
        client.subscribe(WORKERS_STATS)
    else:
        logger.error(f"Échec de la connexion. Code de retour = {rc}")


def on_disconnect(client, userdata, rc):
    if rc != 0:
        logger.info(f"Déconnexion inattendue. Code de retour = {rc}")
    else:
        logger.info("Déconnexion du broker MQTT")


def on_message(client, userdata, msg):
    payload = eval(msg.payload.decode())

    try:
        data = (payload["cpu_usage"], payload["mem_usage"])
        worker = payload["worker"]
        WorkersStats.set_stats_value(k=worker, v=data)
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des stats: {e}")

    if len(WorkersStats.stats) == N_WORKERS:
        WorkersStats.done()


def on_publish(client, userdata, mid):
    logger.info(f"Message publié avec ID {mid}")


def on_subscribe(client, userdata, mid, granted_qos):
    logger.info(f"Abonnement au topic avec ID {mid} et QoS {granted_qos}")


def ping_workers(client):
    for topic in WORKERS_PING:
        try:
            client.publish(topic[0], PING_MSG)
        except Exception as e:
            logger.error(f"Erreur lors du ping: {e}")

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
        dispose(client)
        raise Exception("Connexion au broker MQTT impossible")

    client.loop_start()

    return client


def dispose(client):
    client.loop_stop()
    client.disconnect()


if __name__ == "__main__":
    print(connect())
