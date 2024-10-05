from modules.allocator.edge import Edge
from modules.allocator.packet import Packet
from settings import PACKET_NUMBER


class Env:
    """
    Classe permettant de représenter l'environnement du FOG
    """

    def __init__(self):
        self.packets = [Packet(idPacket=i) for i in range(PACKET_NUMBER)]

        # TODO: à adapter pour récup les données des edges nodes
        # try:
        #     edges_cursor = self.db['edgesLoads'].find()
        #
        #     ide = 0
        #     for edge in edges_cursor:
        #         self.edges.append(Edge(...))
        #         ide += 1
        #
        #     self.m = len(self.edges)
        # except Exception as e:
        #     logger.error('Erreur lors de la récupération des stats des edges dans la base de données: %s', str(e))
        #     exit(1)

        # TESTS
        self.edges = [Edge(ide=0, load=5, remainingStorage=1024*1, uuid='uuid1'),
                      Edge(ide=1, load=80, remainingStorage=1024*10, uuid='uuid2'),
                      Edge(ide=2, load=20, remainingStorage=1024*1000, uuid='uuid3')]


