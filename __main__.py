# from modules.allocator import DLB
from modules.allocator import LB
from modules.allocator.edge import Edge


if __name__ == '__main__':
    # TESTS
    edges = [Edge(ide=0, load=5, remainingStorage=1024 * 1, associated_topic='edge1-topic'),
             Edge(ide=1, load=80, remainingStorage=1024 * 10, associated_topic='edge2-topic'),
             Edge(ide=2, load=20, remainingStorage=1024 * 1000, associated_topic='edge2-topic')]

    lb = LB.LB(name="LB", edges=edges)

    print('\nEdges:')
    for edge in edges:
        print(edge)

    res = lb.solve()
    print("\nResult with edge names:")
    for k, v in res.items():
        if v > 0:
            print(f"{v} packets must be allocated to {k}")
