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

if __name__ == '__main__':
    client = conn_loop(mqtt.connect)
    socket_conn = conn_loop(smp.connect)

    mqtt.WorkersStats.get_stats()

    ide = 0
    edges = []
    for k, v in mqtt.WorkersStats.stats.items():
        edges.append(Edge(ide=ide, load=float(v[0]), remainingStorage=int(v[1]), associated_topic=k))
        ide += 1

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

            smp.publish_policy(socket_conn, res)

            logger.info("------------------------------")
            mqtt.WorkersStats.waiting_stats = False
            sleep(FREQ)
            mqtt.WorkersStats.get_stats()
            lb.update_edges(edges)

    except KeyboardInterrupt:
        logger.info("\nX-X")

    except Exception as e:
        logger.error(f"Erreur: {e}")

    finally:
        mqtt.dispose(client)
        smp.dispose(socket_conn)
        pass
