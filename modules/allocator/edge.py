class Edge:
    def __init__(self, ide: int, load: float, remainingStorage: int, associated_topic: str):
        """
        :param ide: id du edge
        :param load: load du edge (%)
        :param remainingStorage: stockage restant
        :param associated_topic: topic MQTT associé au edge
        """
        self.ide = ide
        self.load = load
        self.remainingStorage = remainingStorage
        self.associated_topic = associated_topic

    def update_stats(self, load: float, remainingStorage: int):
        self.load = load
        self.remainingStorage = remainingStorage

    def __str__(self):
        return f"Edge {self.ide} - Load: {self.load} - Remaining storage: {self.remainingStorage} bits"
