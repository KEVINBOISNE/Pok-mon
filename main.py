from pokemonTrainer import PokemonTrainer
import game_class

print(" === Bienvenue dans le monde des Pokémon ! ===\n")

gameStart =  int (input ("Commencer la partie ?"))
if gameStart ==0:
    print("A bientôt, futur dresseur !")
    exit()

print("sélectionez votre dresseur pokémon")
print("1. Sacha")
print("2. Pierre")
print("3. Ondine")

selectPokemontrainer = int( input ("Entrez le numéro de votre choix la sélection votre dresseur pokémon"))

if selectPokemontrainer ==0:
    print("A bientôt, futur dresseur !")
    exit()

if selectPokemontrainer == 1:
    trainer_name = "Sacha"
if selectPokemontrainer == 2:
    trainer_name = "Pierre"
if selectPokemontrainer == 3:
    trainer_name = "Ondine"

    trainer_name = PokemonTrainer("Sacha")
    trainer_name = PokemonTrainer("Pierre")
    trainer_name = PokemonTrainer("Ondine")
print(f"Vous avez selectionnez PokemonTrainer {trainer_name} ")




#print("Je suis Calvin, jeune dresseur de Pokémon en route vers la ligue régionale d'Avelia, prêt à prouver ma valeur et à devenir le meilleur !")
#print("Je vais affronter, mon premier maitre d'arène qui se nomme Garisson.")
#print("je franchi les portes de l'arène et défi garisson en duel afin de pouvoir remporter mon premier badge")
#print("Se combat nécessite l'affrontemant de 1 Pokémon. Je choisi Dracofeu ! et mon adversaire bulbizarre !")