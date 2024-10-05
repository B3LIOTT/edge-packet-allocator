from docplex.mp.model import Model
from modules.allocator.packet import Packet
from modules.allocator.env import Env
from settings import PACKET_SIZE

# --------fix---------
# pip install "numpy<2"
import numpy as np
np.float_ = np.float64
# --------------------


class LB:
    """
    Problème de load balancing
    """

    def __init__(self, name: str, ENV: Env):
        """
        :param name: nom du problème
        :param ENV: environnement
        """
        # Définition des variables
        self.n = len(ENV.packets)
        self.m = len(ENV.edges)
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
                range_n) <= ENV.edges[j].remainingStorage
            )
        # ----------------------------

        # ---- Fonction objective ----
        self.model.minimize(self.model.sum(
            self.model.sum(
                (ENV.edges[j].load**2) * x_dict[i, j] for j in range_m
            ) for i in range_n
        ))
        # ----------------------------

    def solve(self):
        try:
            self.model.solve(log_output=False)
            x = self.model.solution
            return {k.name.split('_')[1]: k.name.split('_')[2] for k, v in x.as_dict().items() if v == 1.0}
        except Exception as e:
            print('Erreur LB: ', str(e))
            return {}

    def print_information(self):
        print(str(self.model.print_information()))

    def print_solution(self):
        print(str(self.model.print_solution()))
