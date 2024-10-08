
PACKET_NUMBER = 256  # nombre de paquets à traiter par ittération
PACKET_SIZE = 1024  # taille d'un paquet
MAX_STORAGE = 1024 * 1000  # taille de stockage max par edge
FREQ = 2  # secondes


# MQTT
BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883

# Récupération des stats des workers
WORKERS_PING = ["wokers/pone", "wokers/ptwo", "wokers/pthree"]
WORKERS_STATS = ["wokers/one", "wokers/two", "wokers/three"]
PING_MSG = "stats"

TEST_MODE = True
