

class Packet:

    def __init__(self, idPacket: int):
        """
        :param idPacket: id du packet
        """
        self.idPacket = idPacket
        self.target = None

    def updateTarget(self, target: str):
        """
        Met à jour la cible du packet
        :param target: cible sous forme d'un topic mqtt (str)
        """
        self.target = target

    def __eq__(self, other):
        return self.idPacket == other.idPacket

    def __str__(self):
        return f"Packet {self.idPacket}"
