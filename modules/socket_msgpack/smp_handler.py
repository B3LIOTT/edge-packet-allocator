import socket
import msgpack
from settings import SOCKET_PORT, SOCKET_ADDR
from log_conf import logger


def connect():
    try:
        socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_conn.connect((SOCKET_ADDR, SOCKET_PORT))
    except Exception as e:
        raise Exception("Connexion au socket impossible")

    return socket_conn


def dispose(socket_conn):
    if socket_conn:
        socket_conn.close()
    else:
        logger.error("Pas de connexion socket à stopper")


def publish_policy(socket_conn, policy):
    try:
        packed_data = msgpack.packb(policy)
        data_len = len(packed_data).to_bytes(4, 'big')
        socket_conn.sendall(data_len)
        socket_conn.sendall(packed_data)

    except socket.error as e:
        logger.error("Erreur lors de l'envoi de la règle: ", e)
    except msgpack.PackValueError as e:
        logger.error("Erreur lors du paquetage de la règle: ", e)
