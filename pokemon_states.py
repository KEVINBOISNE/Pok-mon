class PokemonStates:
    def __init__ (self, name, level, lifePoint, type):
        self.name = name
        self.level = level
        self.lifePoint = lifePoint
        self.type = type

    def __str__(self):
        return f"{self.name} {self.level} {self.lifePoint} {self.type}"
    