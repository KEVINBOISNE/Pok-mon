class PokemonTeam:
    def __init__(self, name, level, lifePoint, type, power):
        self.name = name
        self.level = level
        self.lifePoint = lifePoint
        self.type = type
        self.power = power

    def __str__(self):
        return f"{self.name} {self.level} {self.lifePoint} {self.type} {self.power}"
    