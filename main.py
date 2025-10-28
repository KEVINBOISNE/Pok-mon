from pokemonTrainer import PokemonTrainer as Train
from difficultyMode import DifficultyMode as Dm
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

selectPokemontrainer = int( input ("Entrez le numéro de votre choix pour la sélection votre dresseur pokémon \n"))

if selectPokemontrainer ==0:
    print("A bientôt, futur dresseur !")
    exit()

if selectPokemontrainer == 1:
    trainer_name = Train("Sacha")
if selectPokemontrainer == 2:
    trainer_name = Train("Pierre")
if selectPokemontrainer == 3:
    trainer_name = Train("Ondine")
    
print(f"Vous avez selectionnez {trainer_name}")


print("Choisiez la difficulté")
print("1.Easy")
print("2.Normal")
print("3.Hard")

difficultyMode = int (input( "Entrez le numéro de votre choix pour la selection de la difficulté"))

if difficultyMode == 0:
    print("A bientôt, futur dresseur !")
    exit()

if difficultyMode == 1:
    difficultyOption = Dm("Easy")
if difficultyMode == 2:
    difficultyOption = Dm("Normal")
if difficultyMode == 3:
    difficultyOption = Dm("Hard")

print(difficultyOption)


#print(f" Je suis {trainer_name}, dresseur de Pokémon en route vers la ligue régionale d'Avelia, prêt à prouver ma valeur et à devenir le meilleur !")
#print("Je dois me rendre chez le professeur Chen obtenir mon premier Pokémon .")

#roads = int (input("Choisiez votre chemin"))

#if roads == 1:
   

#print("Je vais affronter, mon premier maitre d'arène qui se nomme Garisson.")
#print("je franchi les portes de l'arène et défi garisson en duel afin de pouvoir remporter mon premier badge")
#print("Se combat nécessite l'affrontemant de 1 Pokémon. Je choisi Dracofeu ! et mon adversaire bulbizarre !")