import os

PACKET_NUMBER = 1024  # nombre de paquets à traiter par ittération
PACKET_SIZE = 1920*1080*3  # taille d'un paquet
MAX_STORAGE = PACKET_SIZE * 1000  # taille de stockage max par edge
FREQ = 1  # secondes


# MQTT
try:
    BROKER_ADDRESS = os.environ.get("BROKER_ADDRESS")
    BROKER_PORT = int(os.environ.get("BROKER_PORT"))
except TypeError:
    BROKER_ADDRESS = "localhost"
    BROKER_PORT = 1883

# Policy
SOCKET_ADDR = ""#os.environ.get("SOCKET_ADDR")
SOCKET_PORT = 1#int(os.environ.get("SOCKET_PORT"))

# Récupération des stats des workers
N_WORKERS = 3
WORKERS_PING = ["ping_worker_1", "ping_worker_2", "ping_worker_3"]
WORKERS_STATS = ["stats_worker_1", "stats_worker_2", "stats_worker_3"]
PING_MSG = "stats"

TEST_MODE = False
