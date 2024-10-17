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
    ide = 0
    new_edges = []
    for key, val in mqtt.WorkersStats.stats.items():
        new_edges.append(Edge(ide=ide, load=float(val[0]), remainingStorage=int(val[1]), associated_topic=key))
        ide += 1

    return new_edges


if __name__ == '__main__':
    logger.info("----------LOAD BALANCER----------")
    #client = conn_loop(mqtt.connect)
    client = None
    logger.info("Connexion au broker MQTT réussie")
    #socket_conn = conn_loop(smp.connect)

    mqtt.WorkersStats.get_stats(client)

    edges = build_edges()

    try:
        lb = LB.LB(name="LB", edges=edges)
        while True:
            if TEST_MODE:
                logger.info('\nEdges:')
                for edge in edges:
                    logger.info(edge)
                logger.info("\nResult:")

            res = lb.solve()

            for k, v in res.items():
                if v > 0:
                    logger.info(f"{k} : {v}")

            #smp.publish_policy(socket_conn, res)

            logger.info("------------------------------")
            sleep(FREQ)
            mqtt.WorkersStats.get_stats(client)
            edges = build_edges()
            lb.update_edges(edges)

    except KeyboardInterrupt:
        logger.info("\nX-X")

    except Exception as e:
        logger.error(f"Erreur main: {e}")

    finally:
        # mqtt.dispose(client)
        # smp.dispose(socket_conn)
        pass
