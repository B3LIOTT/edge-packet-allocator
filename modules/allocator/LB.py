import numpy as np
from modules.allocator.edge import Edge
from settings import PACKET_SIZE, PACKET_NUMBER, MAX_STORAGE, CPU_THRESHOLD
from log_conf import logger


class LB:
    """
    Problème de load balancing
    """

    def __init__(self, name: str):
        """
        :param name: nom du problème
        """
        self.edges = []
        self.bounds = (CPU_THRESHOLD, MAX_STORAGE - PACKET_SIZE)

    def update_edges(self, edges: list[Edge]):
        self.edges = edges
        logger.info('Edges mis à jour:')
        for edge in edges:
            logger.info(edge)


    def solve(self) -> dict[str, int]:
        try:
            allocation_dict = {}
            good_edges = []
            tot = 0
            for e in self.edges:
                if e.load < self.bounds[0] and (MAX_STORAGE - e.remainingStorage) < self.bounds[1]:
                    weight = 1/np.sqrt( (e.load/100)**3 + (e.remainingStorage/MAX_STORAGE)**2)
                    good_edges.append((e, weight))
                    tot += weight

            if len(good_edges) == 0:
                logger.error('Erreur LB: Aucun edge disponible')
                return {}

            for e, weight in good_edges:
                pNum = int(PACKET_NUMBER * weight / tot)
                allocation_dict[e.associated_topic] = pNum if e.remainingStorage > pNum else e.remainingStorage // PACKET_SIZE

            return allocation_dict
        except Exception as e:
            logger.error('Erreur LB: ', str(e))
            return {}

