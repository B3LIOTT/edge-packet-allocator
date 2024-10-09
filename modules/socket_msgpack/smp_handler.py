from settings import POLICY_SOCKET_ADR, POLICY_SOCKET_PORT
import socket
import msgpack


def connect():
    try:
        socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_conn.connect((POLICY_SOCKET_ADR, POLICY_SOCKET_PORT))
    except Exception as e:
        print("Erreur lors de la connexion socket au server: ", e)
        exit(1)

    return socket_conn


def dispose(socket_conn):
    if socket_conn:
        socket_conn.close()
    else:
        print("Pas de connexion socket à stopper")


def publish_policy(socket_conn, policy):
    try:
        packed_data = msgpack.packb(policy)
        socket_conn.sendall(packed_data)
        print(f"Sent data: {policy}")

    except socket.error as e:
        print("Erreur lors de l'envoi de la règle: ", e)
    except msgpack.PackValueError as e:
        print("Erreur lors du paquetage de la règle: ", e)
