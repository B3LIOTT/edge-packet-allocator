from modules.allocator import LB
from modules.allocator.edge import Edge
from modules.mqtt import mqtt_handler as mqtt


if __name__ == '__main__':
    edges = []
    stats = mqtt.run()
    ide = 0
    for k, v in stats.items():
        edges.append(Edge(ide=ide, load=float(v[0]), remainingStorage=int(v[1]), associated_topic=k))
        ide += 1

    lb = LB.LB(name="LB", edges=edges)

    print('\nEdges:')
    for edge in edges:
        print(edge)

    res = lb.solve()
    print("\nResult with edge names:")
    for k, v in res.items():
        if v > 0:
            print(f"{v} packets must be allocated to {k}")
