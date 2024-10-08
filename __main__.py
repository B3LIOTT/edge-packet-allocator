from modules.allocator import LB
from modules.allocator.edge import Edge
from modules.mqtt import mqtt_handler as mqtt
from settings import TEST_MODE
from time import sleep


if __name__ == '__main__':
    stats = mqtt.run()

    ide = 0
    edges = []
    for k, v in stats.items():
        edges.append(Edge(ide=ide, load=float(v[0]), remainingStorage=int(v[1]), associated_topic=k))
        ide += 1

    if TEST_MODE:
        print('\nEdges:')
        for edge in edges:
            print(edge)
        print("\nResult:")

    try:
        while True:
            lb = LB.LB(name="LB", edges=edges)
            res = lb.solve()

            for k, v in res.items():
                if v > 0:
                    print(f"{k} : {v}")

            print("------------------------------")
            sleep(2)

    except KeyboardInterrupt:
        print("\nX-X")
        exit(0)
