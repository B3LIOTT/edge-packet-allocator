import os

PACKET_NUMBER = 300  # nombre de paquets à traiter par ittération
PACKET_SIZE = 2000000  # taille d'un paquet en octets
MAX_STORAGE = 10**9 # taille de stockage max par edges en octets
FREQ = 1  # secondes


# MQTT
try:
    BROKER_ADDRESS = os.environ.get("BROKER_ADDRESS")
    BROKER_PORT = int(os.environ.get("BROKER_PORT"))
except TypeError:
    BROKER_ADDRESS = "10.8.13.94"
    BROKER_PORT = 1883

# Policy
try:    
    SOCKET_ADDR = os.environ.get("SOCKET_ADDR")
    SOCKET_PORT = int(os.environ.get("SOCKET_PORT"))
except TypeError:
    SOCKET_ADDR = "10.8.13.94"
    SOCKET_PORT = 8081

# Récupération des stats des workers
N_WORKERS = 3
WORKERS_PING = [("worker-node-1-ping", 1), ("worker-node-2-ping", 1), ("worker-node-3-ping", 1)]
WORKERS_STATS = [("worker-node-1-stats", 1), ("worker-node-2-stats", 1), ("worker-node-3-stats", 1)]
PING_MSG = "stats"

TEST_MODE = False
