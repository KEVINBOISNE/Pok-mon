class PokemonStates():
    
    def __init__ (self, name, level, lifePoint, type, power):
        self.name = name
        self.level = level
        self.lifePoint = int(lifePoint.split()[0])
        self.type = type
        self.power = int(power.split()[0])

    def __str__(self):
        return f"{self.name} {self.level} {self.lifePoint} {self.type} {self.power}"

class WildPokemon(PokemonStates):
    pass
    
class PokemonTeam(PokemonStates):
    pass

