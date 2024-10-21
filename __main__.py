from modules.allocator import LB
from modules.allocator.edge import Edge
from modules.mqtt import mqtt_handler as mqtt
from modules.socket_msgpack import smp_handler as smp
from settings import TEST_MODE, FREQ
from time import sleep
from log_conf import logger


def conn_loop(call):
    while True:
        try:
            ret = call()
            break
        except Exception as e:
            logger.error(f"Erreur: {e}")
            sleep(1)
        except KeyboardInterrupt:
            logger.info("\nX-X")
            exit(0)

    return ret


def build_edges():
    new_edges = []
    for key, val in mqtt.WorkersStats.stats.items():
        new_edges.append(Edge(load=float(val[0]), remainingStorage=int(val[1]), associated_topic=key))

    return new_edges


if __name__ == '__main__':
    client = conn_loop(mqtt.connect)
    socket_conn = conn_loop(smp.connect)
    mqtt.WorkersStats.get_stats(client)
    edges = build_edges()

    try:
        lb = LB.LB(name="LB")
        lb.update_edges(edges)
        while True:
            res = lb.solve()
            logger.info(f"Result: {res}")
            smp.publish_policy(socket_conn, res)

            sleep(FREQ)
            mqtt.WorkersStats.get_stats(client)
            logger.info(f"Worker stats: {mqtt.WorkersStats.stats}")
            edges = build_edges()
            lb.update_edges(edges)

    except KeyboardInterrupt:
        logger.info("\nX-X")

    except Exception as e:
        logger.error(f"Erreur main: {e}")

    finally:
        mqtt.dispose(client)
        smp.dispose(socket_conn)
