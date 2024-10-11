from modules.allocator import LB
from modules.allocator.edge import Edge
from modules.mqtt import mqtt_handler as mqtt
from modules.socket_msgpack import smp_handler as smp
from settings import TEST_MODE, FREQ
from time import sleep


if __name__ == '__main__':
    # client = mqtt.connect()
    # socket_conn = smp.connect()
    mqtt.WorkersStats.get_stats()

    ide = 0
    edges = []
    for k, v in mqtt.WorkersStats.stats.items():
        edges.append(Edge(ide=ide, load=float(v[0]), remainingStorage=int(v[1]), associated_topic=k))
        ide += 1

    try:
        while True:
            if TEST_MODE:
                print('\nEdges:')
                for edge in edges:
                    print(edge)
                print("\nResult:")

            lb = LB.LB(name="LB", edges=edges)
            res = lb.solve()

            for k, v in res.items():
                if v > 0:
                    print(f"{k} : {v}")

            # smp.publish_policy(socket_conn, res)

            print("------------------------------")
            mqtt.WorkersStats.waiting_stats = False
            sleep(FREQ)
            mqtt.WorkersStats.get_stats()

    except KeyboardInterrupt:
        print("\nX-X")

    except Exception as e:
        print(f"Erreur: {e}")

    finally:
        # mqtt.dispose(client)
        # smp.dispose(socket_conn)
        pass
