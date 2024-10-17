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
        self.n = PACKET_NUMBER
        self.m = len(edges)
        range_n = range(self.n)
        range_m = range(self.m)
        indx = [(i, j) for i in range_n for j in range_m]

        # Modèle
        self.model = Model(name=name)
        x_dict = self.model.binary_var_dict(indx, name="x")

        # ---- Contraintes ----
        # Allocation
        for i in range_n:
            self.model.add_constraint(self.model.sum(x_dict[i, j] for j in range_m) == 1)

        # Capacité de stockage des fog nodes
        for j in range_m:
            self.model.add_constraint(self.model.sum(
                PACKET_SIZE * x_dict[i, j] for i in
                range_n) <= edges[j].remainingStorage
                                      )
        # ----------------------------

        # ---- Fonction objective ----
        self.model.minimize(self.model.sum(
            self.model.sum(
                edges[j].load * x_dict[i, j] for j in range_m
            ) for i in range_n
        ))
        # ----------------------------


    def update_edges(self, edges: list[Edge]):
        self.edges = edges

    def solve(self) -> dict[str, int]:
        try:
            self.model.solve(log_output=False)
            x = self.model.solution
            allocation_dict = {}
            for k, v in x.as_dict().items():
                if v == 1.0:
                    target = getEdgeNameFromID(int(k.name.split('_')[2]), self.edges)
                    allocation_dict[target] = 1 if target not in allocation_dict else allocation_dict[target] + 1

            return allocation_dict
        except Exception as e:
            logger.error('Erreur LB: ', str(e))
            return {}

    def print_information(self):
        print(str(self.model.print_information()))

    def print_solution(self):
        print(str(self.model.print_solution()))
