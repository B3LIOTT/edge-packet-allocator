# from modules.allocator import DLB
from modules.allocator import LB
from modules.allocator import env
import sys


if __name__ == '__main__':
    ENV = env.Env()
    lb = LB.LB(name="LB", ENV=ENV)

    print('Packets:')
    for packet in ENV.packets:
        print(packet)

    print('\nEdges:')
    for edge in ENV.edges:
        print(edge)

    res = lb.solve()
    print(res)
