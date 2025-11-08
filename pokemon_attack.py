class PokemonAttack:
    def __init__(self, attack, power):
        self.attack = attack
        self.power = power

    def __str__(self):
        return f"{self.attack} {self.power}"