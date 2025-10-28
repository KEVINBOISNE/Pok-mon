from pokemonTrainer import PokemonTrainer as Train
from difficultyMode import DifficultyMode as Dm
from roads import Roads as Rds
from pokemon_states import PokemonStates as Ps
import game_class

print(" === Bienvenue dans le monde des Pokémon ! ===\n")

gameStart =  int (input ("Commencer la partie ?"))
if gameStart ==0:
    print("A bientôt, futur dresseur !")
    exit()

print("Sélectionez votre dresseur pokémon")
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


print(f"Je suis {trainer_name}, dresseur de Pokémon en route vers la ligue régionale de Kanto, prêt à prouver ma valeur et à devenir le meilleur !")
print("Je dois me rendre chez le professeur CHEN obtenir mon premier Pokémon .")

print("Sélectionez le chemin dont vous souhaitez vous rendre")
print("1.Chez professeur CHEN")

roads = int (input("Entrez le numéro de votre choix pour la sélection du chemin"))

if roads == 1:
    roadsOption = Rds("Chez professeur CHEN")
#if roads == 2:
   # roadsOption = Rds("Dans les hautes herbes")
#if roads == 3:
  #  roadsOption = Rds ("Arène d'Azuria")

print(roadsOption)
   

print("Bonjour Professeur CHEN, je viens pour obtenir mon premier pokémon")   
print(f"Bonjour {trainer_name}, tu arrives au bon moment. Tu as le choix entre ces trois pokémon")
print("Sélectionez le pokémon dont vous souhaitez voir les statistiques")

array = []
choiceConfirm = False

while not choiceConfirm:
    print("1.Pikachu")
    print("2.Salamèche")
    print("3.Bulbizarre")
    print("4.Carapuce")

    pokemonStatistics = int (input("Entrez le numéro de votre choix pour la sélection du pokémon" ))
    if pokemonStatistics == 1:
        pokemonStats = Ps ("Pikachu", "5 Lvl" , "50 LP" , "Electrik")
    if pokemonStatistics == 2:
        pokemonStats = Ps ("Salamèche", "5 Lvl" , "60 Lvl", "Fire")
    if pokemonStatistics == 3:
        pokemonStats = Ps ("Bulbizarre","5 Lvl" , "55 Lvl", "Plant")
    if pokemonStatistics == 4:
        pokemonStats = Ps ("Carapuce", "5 Lvl" , "70 Lvl" , "Water")

    print(f"{pokemonStats}")
        
    print(f"Vous avez choisi {pokemonStats}")
    print("Souhaitez-vous garder ce Pokémon ?")
    print("1.Oui")
    print("2.Non")
    keepPokemon = int (input("Entrez le numéro de votre choix pour obtenir ce pokémon "))


    if keepPokemon == 1:
        choiceConfirm=True
        array.append(array) 
        print(f"Parfait ! {pokemonStats.name} rejoint votre équipe !")
    else:
        print("Très bien, vous pourrez choisir un autre Pokémon plus tard.")
                         
print(f"CHEN: Félicitation {trainer_name}, Tu viens d'obtenir ton premier pokémon")
print("CHEN: Je te conseil, d'entrainer ton pokémon afin de pouvoir affroter le maitre d'arène d'Azuria")
print("CHEN: A moins que tu sois sur de toi et de tenté ta chance dans l'arène qui détient, trois étages avec un dresseur les uns plus fort que les autres !")
print(f"CHEN: Bonne chance {trainer_name}")
print("Je dois me rendre chez le professeur CHEN obtenir mon premier Pokémon")

print("Sélectionez le chemin dont vous souhaitez vous rendre")
print("1.Dans les hautes herbes")
print("2.Arène d'Azuria")

roads = int (input("Entrez le numéro de votre choix pour la sélection du chemin"))

if roads == 1:
    roadsOption = Rds("Dans les hautes herbes")
if roads == 2:
   roadsOption = Rds ("Arène d'Azuria")

print(roadsOption)





#print("Je vais affronter, mon premier maitre d'arène qui se nomme Garisson.")
#print("je franchi les portes de l'arène et défi garisson en duel afin de pouvoir remporter mon premier badge")
#print("Se combat nécessite l'affrontemant de 1 Pokémon. Je choisi Dracofeu ! et mon adversaire bulbizarre !")