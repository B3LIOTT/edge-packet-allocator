
PACKET_NUMBER = 256  # nombre de paquets à traiter par ittération
PACKET_SIZE = 1920*1080*3  # taille d'un paquet
MAX_STORAGE = PACKET_SIZE * 1000  # taille de stockage max par edge
FREQ = 1  # secondes


# MQTT
BROKER_ADDRESS = "123abc"
BROKER_PORT = 1883

# Policy
POLICY_TOPIC = "LB_policy"
SOCKET_ADDR = "192.168.202.80"
SOCKET_PORT = 8000

# Récupération des stats des workers
N_WORKERS = 3
WORKERS_PING = ["ping_worker_1", "ping_worker_2", "ping_worker_3"]
WORKERS_STATS = ["stats_worker_1", "stats_worker_2", "stats_worker_3"]
PING_MSG = "stats"

TEST_MODE = False
