class Bag:
    def __init__(self, object, energy, quantity):
        self.object = object
        self.energy = energy
        self.quantity = quantity

    def __str__(self):
        return f"{self.object} {self.energy} {self.quantity}"
        