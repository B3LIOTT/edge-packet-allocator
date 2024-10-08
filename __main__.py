from modules.allocator import LB
from modules.allocator.edge import Edge
from modules.mqtt import mqtt_handler as mqtt
from settings import TEST_MODE
from time import sleep


if __name__ == '__main__':
    client = mqtt.connect()
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

            print("------------------------------")
            sleep(2)
            mqtt.WorkersStats.get_stats()

    except KeyboardInterrupt:
        print("\nX-X")
        # mqtt.dispose(client)
        exit(0)

    except Exception as e:
        print(f"Erreur: {e}")
        # mqtt.dispose(client)
        exit(1)
