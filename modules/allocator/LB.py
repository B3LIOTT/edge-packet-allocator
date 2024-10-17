from docplex.mp.model import Model
from modules.allocator.edge import Edge
from settings import PACKET_SIZE, PACKET_NUMBER
from modules.allocator.utils import getEdgeNameFromID
from log_conf import logger

# --------fix---------
# pip install "numpy<2"
import numpy as np
np.float_ = np.float64
# --------------------


class LB:
    """
    Problème de load balancing
    """

    def __init__(self, name: str, edges: list[Edge]):
        """
        :param name: nom du problème
        :param ENV: environnement
        """
        # Définition des variables
        self.edges = edges
        logger.info(f"\nEdges: {[edge.load for edge in edges]}\n")
        self.n = PACKET_NUMBER
        self.m = len(edges)
        range_n = range(self.n)
        range_m = range(self.m)


    def update_edges(self, edges: list[Edge]):
        self.edges = edges
        logger.info('Edges mis à jour:')
        for edge in edges:
            logger.info(edge)


    def solve(self) -> dict[str, int]:
        try:
            allocation_dict = {}

            return allocation_dict
        except TypeError or AttributeError:
            logger.error('Erreur LB: Aucune solution trouvée')
            return {}
        except Exception as e:
            logger.error('Erreur LB: ', str(e))
            return {}

