class Edge:
    def __init__(self, ide: int, load: float, remainingStorage: int, uuid: str):
        """
        :param ide: id du edge
        :param load: load du edge
        :param remainingStorage: stockage restant
        """
        self.ide = ide
        self.load = load
        self.remainingStorage = remainingStorage
        self.uuid = uuid

    def __eq__(self, other):
        return self.ide == other.ide

    def __str__(self):
        return f"Edge {self.ide} - Load: {self.load} - Remaining storage: {self.remainingStorage} bits"
