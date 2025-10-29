from pokemonTrainer import PokemonTrainer as Train
from difficultyMode import DifficultyMode as Dm
from roads import Roads as Rds
from pokemonStates import PokemonStates as Ps
from wildPokemon  import WildPokemon as Wp
from pokemon_attack import PokemonAttack as Pa
import random
from bag import Bag as Bg

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

arrayTeamPokemon = []
arrayBag = []
choiceConfirm = False

pokeBall = Bg (f"pokeball", "", 5)
potion = Bg (f"postion", "35 Lp", 5)


while not choiceConfirm:
    print("1.Pikachu")
    print("2.Salamèche")
    print("3.Bulbizarre")
    print("4.Carapuce")

    pokemonStatistics = int (input("Entrez le numéro de votre choix pour la sélection du pokémon" ))
    if pokemonStatistics == 1:
        pokemonStats = Ps ("Pikachu", "5 Lvl" , "50 LP" , "Electrik", "10")
    elif pokemonStatistics == 2:
        pokemonStats = Ps ("Salamèche", "5 Lvl" , "60 Lvl", "Fire", "15")
    elif pokemonStatistics == 3:
        pokemonStats = Ps ("Bulbizarre","5 Lvl" , "55 Lvl", "Plant", "11")
    elif pokemonStatistics == 4:
        pokemonStats = Ps ("Carapuce", "5 Lvl" , "70 Lvl" , "Water", "13")

    print(f"{pokemonStats}")
        
    print(f"Vous avez choisi {pokemonStats}")
    print("Souhaitez-vous garder ce Pokémon ?")
    print("1.Oui")
    print("2.Non")
    keepPokemon = int (input("Entrez le numéro de votre choix pour obtenir ce pokémon "))


    if keepPokemon == 1:
        choiceConfirm=True
        arrayTeamPokemon.append(pokemonStats.name) 
        print(f"Parfait ! {pokemonStats.name} rejoint votre équipe !")
    else:
        print("Très bien, vous pourrez choisir un autre Pokémon plus tard.")
                         
print(f"CHEN: Félicitation {trainer_name}, Tu viens d'obtenir ton premier pokémon")
print(f"CHEN: Comme je suis gentil, je te donne également 5 pokéballs, 5 potions.")
arrayBag.append(pokeBall)
arrayBag.append(potion)

print(f"{trainer_name} recoit 5 pokéballs et 5 potions !")
print("CHEN: Je te conseil, d'entrainer ton pokémon afin de pouvoir affroter le maitre d'arène d'Azuria")
print("CHEN: A moins que tu sois sur de toi, et de tenter ta chance dans l'arène qui détient, trois étages avec un dresseur les uns plus fort que les autres !")
print(f"CHEN: Bonne chance {trainer_name}")


print("Sélectionez le chemin dont vous souhaitez vous rendre")
print("1.Dans les hautes herbes")
print("2.Arène d'Azuria")

roads = int (input("Entrez le numéro de votre choix pour la sélection du chemin"))

if roads == 1:
    roadsOption = Rds("Dans les hautes herbes")
elif roads == 2:
   roadsOption = Rds ("Arène d'Azuria")

print(roadsOption)

if roads == 1:
    print("Un pokemon sauvage apparait ! Souhaitez vous le combattre ?")
    print("1.Combattre")
    print("2.fuir")

    meetingPokemon = int (input("Entrez le numéro de votre choix pour la prise de descision" ))

    if meetingPokemon == 1:

        playerPokemon = Ps ("Pikachu", "5 Lvl" , "50 LP" , "Electrik", "10")
        wildPokemon = Wp ("Rattata", "3 Lvl" , "47 LP" , "Normal", "7")

        print(f"J'appelle {playerPokemon.name} à l'attaque !")
        print(f"{wildPokemon.name} rattata Grrr")

        endFight = False
        while not endFight:
            print("Choisissez une attaque :")
            print("1.Griffe")
            print("2.Rugissement")
            print("3.Sac")
       
            pokemonFight = int (input("Entrez le numéro de l'attaque que vous voulez effectuer:"))
            if pokemonFight == 1:
                pokemonAttack = Pa ("Griffe", 10)
                wildPokemon.lifePoint -= pokemonAttack.power
                print(f"{playerPokemon.name} utilise {pokemonAttack.attack} !")
                print(f"{wildPokemon.name} perd {pokemonAttack.power} Lp !")
                print(f"Lp restants de {wildPokemon.name}: {wildPokemon.lifePoint}")

            elif pokemonFight == 2:
                pokemonAttack = Pa("Rugissement", 0)
                wildPokemon.power = max(1, wildPokemon.power -2)
                print(f"{playerPokemon.name} utilise {pokemonAttack.attack} !")
                print(f"{wildPokemon.name} voit son attaque baisser {wildPokemon.power} !")

            elif pokemonFight == 3:
                print("Choisissez un objet:")
                for i in range(len(arrayBag)):
                    print(f"{i+1}. {arrayBag[i].object} x{arrayBag[i].quantity}")
                print("3. Retour")
                
                arrayBagObject = int (input("Entrez le numéro de l'objet que vous voulez utiliser:") )

                if arrayBagObject == 1:
                    if pokeBall.quantity > 0:
                        pokeBall.quantity -= 1
                    print(f"Vous lancez une Pokéball sur {wildPokemon.name} !")
                    catchChance = random.randint(1, 3)
                    if catchChance == 1:
                        print(f"Félicitations ! vous avez capturé {wildPokemon.name} !")
                        arrayTeamPokemon.append(wildPokemon.name)
                        endFight = True
                        break
                else:
                    print(f"{wildPokemon} s'est échappé")

                if arrayBagObject == 2:
                    if potion.quantity > 0:
                        potion.quantity -= 1
                        print(f"Vous utiliser une potion sur {playerPokemon} !")
                        playerPokemon.lifePoint += 35
                        print(f"{playerPokemon.name} à récupérer {playerPokemon.lifePoint} lp") 
                 
                
            if  wildPokemon.lifePoint <= 0:    
                endFight = True
                print(f"{playerPokemon.name} à battu le {wildPokemon.name} sauvage !")
                break
            
            randomAttack = random.randint(1, 3)

            if randomAttack == 1:
                wildPokemonAttack = Pa ("Rugissement", 0)
                playerPokemon.power = max(1, playerPokemon.power -2)
                print(f"{wildPokemon.name} utilise {wildPokemonAttack.attack} ! ")
                print(f"{playerPokemon.name} voit son attaque baisser {playerPokemon.power} !")
            else:
                wildPokemonAttack = Pa ("Morsure", 7)
                print(f"{wildPokemon.name} riposte !")
                print (f"{wildPokemon.name} attaque avec Morsure ! ")
                playerPokemon.lifePoint -= wildPokemonAttack.power
                print(f"{playerPokemon.name} perd {wildPokemonAttack} Lp")
                print(f"PV restants de {playerPokemon.name} : {playerPokemon.lifePoint}")
            

            if playerPokemon.lifePoint <= 0:
                endFight = True
                print(f"{wildPokemon.name} à battu {playerPokemon.name} ! ")
                break

    elif meetingPokemon == 2:
        print("Vous avez choisi de fuir le combat.")

else:
    print("Bienvenue dans l'arène d'Azuria !")


    
   

                
#print("Je vais affronter, mon premier maitre d'arène qui se nomme Garisson.")
#print("je franchi les portes de l'arène et défi garisson en duel afin de pouvoir remporter mon premier badge")
#print("Se combat nécessite l'affrontemant de 1 Pokémon. Je choisi Dracofeu ! et mon adversaire bulbizarre !")