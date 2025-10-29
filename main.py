from pokemonTrainer import PokemonTrainer as Train
from difficultyMode import DifficultyMode as Dm
from roads import Roads as Rds
from pokemonStates import PokemonStates as Ps
from wildPokemon  import WildPokemon as Wp
from pokemon_attack import PokemonAttack as Pa
from pokemonTeam import PokemonTeam as Pt
import random
from bag import Bag as Bg

print(" === Bienvenue dans le monde des Pokémon ! ===\n")
arrayTeamPokemon = []

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
if roads == 2 and arrayTeamPokemon == 0 :
        roadsOption = Rds("Dans les hautes herbes")
else:
        print("pas possible")
if roads == 3 and arrayTeamPokemon == 0 :
        roadsOption = Rds ("Arène d'Azuria")
else:
    print("pas possible")
    

    print(roadsOption)

    print("Bonjour Professeur CHEN, je viens pour obtenir mon premier pokémon")   
    print(f"Bonjour {trainer_name}, tu arrives au bon moment. Tu as le choix entre ces trois pokémon")
    print("Sélectionez le pokémon dont vous souhaitez voir les statistiques")


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
            pokemonStats = Ps ("Salamèche", "5 Lvl" , "1000 LP", "Fire", "1000")
        elif pokemonStatistics == 3:
            pokemonStats = Ps ("Bulbizarre","5 Lvl" , "55 LP", "Plant", "11")
        elif pokemonStatistics == 4:
            pokemonStats = Ps ("Carapuce", "5 Lvl" , "70 LP" , "Water", "13")

        print(f"{pokemonStats}")
            
        print(f"Vous avez choisi {pokemonStats}")
        print("Souhaitez-vous garder ce Pokémon ?")
        print("1.Oui")
        print("2.Non")

        keepPokemon = int (input("Entrez le numéro de votre choix pour obtenir ce pokémon "))


        if keepPokemon == 1:
            choiceConfirm=True
            arrayTeamPokemon.append(pokemonStats) 
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


# Boucle principale des arènes après l'obtention du premier Pokémon
while True:
    print("Sélectionez le chemin dont vous souhaitez vous rendre")
    print("1.Dans les hautes herbes")
    print("2.Arène d'Azuria")
    print("3.Arène de Céladopole")
    print("4.Arène de Cramois'Île")
    roads = int(input("Entrez le numéro de votre choix pour la sélection du chemin: "))

    # ========================
    # CHEMIN : Hautes herbes
    # ========================
    if roads == 1:
        roadsOption = Rds("Dans les hautes herbes")
        print(roadsOption)
        print("Un Pokémon sauvage apparaît ! Souhaitez-vous le combattre ?")
        print("1.Combattre")
        print("2.Fuir")
        meetingPokemon = int(input("Entrez le numéro de votre choix: "))
        if meetingPokemon == 1:
            playerPokemon = arrayTeamPokemon[0]
            wildPokemon = Wp("Rattata", "3 Lvl", "47 LP", "Normal", "7")
            
            endFight = False
            while not endFight:
                print("Choisissez une attaque :")
                print("1.Griffe")
                print("2.Rugissement")
                print("3.Équipe")
                print("4.Sac")
                pokemonFight = int(input("Numéro de l'attaque: "))

                if pokemonFight == 1:
                    pokemonAttack = Pa("Griffe", 1000)
                    wildPokemon.lifePoint -= pokemonAttack.power
                    print(f"{playerPokemon.name} utilise {pokemonAttack.attack} !")
                    print(f"{wildPokemon.name} perd {pokemonAttack.power} LP !")

                elif pokemonFight == 2:
                    pokemonAttack = Pa("Rugissement", 0)
                    wildPokemon.power = max(1, wildPokemon.power - 2)
                    print(f"{playerPokemon.name} utilise {pokemonAttack.attack} !")
                    print(f"{wildPokemon.name} voit son attaque baisser à {wildPokemon.power} !")

                elif pokemonFight == 3:
                    print("Choisissez un Pokémon:")
                    for i, pt in enumerate(arrayTeamPokemon):
                        print(f"{i+1}. {pt.name} {pt.level} {pt.lifePoint} {pt.type} {pt.power}")
                    arrayTeamPokemons = int(input("Numéro du Pokémon: "))
                    if 1 <= arrayTeamPokemons <= len(arrayTeamPokemon):
                        selectedPokemon = arrayTeamPokemon[arrayTeamPokemons - 1]
                        if selectedPokemon.lifePoint > 0:
                            playerPokemon = selectedPokemon
                            print(f"{playerPokemon.name} entre en scène !")
                        else:
                            print(f"{selectedPokemon.name} est K.O et ne peut pas combattre !")

                elif pokemonFight == 4:
                    print("Choisissez un objet :")
                    for i, obj in enumerate(arrayBag):
                        print(f"{i+1}. {obj.object} x{obj.quantity}")
                    arrayBagObject = int(input("Numéro de l'objet: "))
                    if arrayBagObject == 2 and potion.quantity > 0:
                        potion.quantity -= 1
                        playerPokemon.lifePoint += 35
                        print(f"{playerPokemon.name} récupère {playerPokemon.lifePoint} LP")

                if wildPokemon.lifePoint <= 0:
                    endFight = True
                    print(f"{playerPokemon.name} a battu {wildPokemon.name} !")
                    break

                # Attaque sauvage
                randomAttack = random.randint(1, 3)
                if randomAttack == 1:
                    wildPokemonAttack = Pa("Rugissement", 0)
                    playerPokemon.power = max(1, playerPokemon.power - 2)
                    print(f"{wildPokemon.name} utilise {wildPokemonAttack.attack} !")
                else:
                    wildPokemonAttack = Pa("Morsure", 7)
                    playerPokemon.lifePoint -= wildPokemonAttack.power
                    print(f"{playerPokemon.name} perd {wildPokemonAttack.power} LP")

                if playerPokemon.lifePoint <= 0:
                    endFight = True
                    print(f"{wildPokemon.name} a battu {playerPokemon.name} !")
        else:
            print("Vous avez choisi de fuir le combat.")

    # ========================
    # ARÈNE D'AZURIA
    # ========================
    if roads == 2:
        print("Bienvenue dans l'arène d'Azuria !")
        unlocked_floors = 1
        while True:
            print("Sélectionnez l'étage :")
            for f in range(1, min(unlocked_floors+1, 6)):
                name = "Premier" if f==1 else "Deuxième" if f==2 else "Troisième" if f==3 else "Quatrième" if f==4 else "Cinquième"
                print(f"{f}. {name} étage")
            floor_choice = int(input("Numéro de l'étage : "))

            if floor_choice <= unlocked_floors:
                if floor_choice == 1: wildPokemon = Wp("Otaria", "8 Lvl", "50 LP", "Water", "7")
                elif floor_choice == 2: wildPokemon = Wp("Poissirène", "9 Lvl", "55 LP", "Water", "7")
                elif floor_choice == 3: wildPokemon = Wp("Amonistar", "10 Lvl", "60 LP", "Water", "8")
                elif floor_choice == 4: wildPokemon = Wp("Têtarte", "11 Lvl", "65 LP", "Water", "9")
                elif floor_choice == 5: wildPokemon = Wp("Lokhlass", "12 Lvl", "70 LP", "Water", "10")

                print(f"Un dresseur vous défie avec {wildPokemon.name} !")

                playerPokemon = arrayTeamPokemon[0]
                endFight = False
                while not endFight:
                    print("Choisissez une attaque : 1.Griffe 2.Rugissement 3.Équipe 4.Sac")
                    pokemonFight = int(input("Numéro de l'attaque: "))

                    if pokemonFight == 1:
                        pokemonAttack = Pa("Griffe", 10)
                        wildPokemon.lifePoint -= pokemonAttack.power
                        print(f"{playerPokemon.name} utilise {pokemonAttack.attack} ! {wildPokemon.name} perd {pokemonAttack.power} LP !")
                    elif pokemonFight == 2:
                        pokemonAttack = Pa("Rugissement", 0)
                        wildPokemon.power = max(1, wildPokemon.power - 2)
                        print(f"{playerPokemon.name} utilise {pokemonAttack.attack} ! {wildPokemon.name} voit son attaque baisser à {wildPokemon.power} !")
                    elif pokemonFight == 3:
                        print("Choisissez un Pokémon:")
                        for i, pt in enumerate(arrayTeamPokemon):
                            print(f"{i+1}. {pt.name} {pt.level} {pt.lifePoint} {pt.type} {pt.power}")
                        arrayTeamPokemons = int(input("Numéro du Pokémon: "))
                        if 1 <= arrayTeamPokemons <= len(arrayTeamPokemon):
                            selectedPokemon = arrayTeamPokemon[arrayTeamPokemons - 1]
                            if selectedPokemon.lifePoint > 0:
                                playerPokemon = selectedPokemon
                                print(f"{playerPokemon.name} entre en scène !")
                            else:
                                print(f"{selectedPokemon.name} est K.O et ne peut pas combattre !")
                    elif pokemonFight == 4:
                        print("Choisissez un objet :")
                        for i, obj in enumerate(arrayBag):
                            print(f"{i+1}. {obj.object} x{obj.quantity}")
                        arrayBagObject = int(input("Numéro de l'objet: "))
                        if arrayBagObject == 2 and potion.quantity > 0:
                            potion.quantity -= 1
                            playerPokemon.lifePoint += 35
                            print(f"{playerPokemon.name} récupère {playerPokemon.lifePoint} LP")

                    if wildPokemon.lifePoint <= 0:
                        endFight = True
                        print(f"{playerPokemon.name} a battu {wildPokemon.name} !")
                        if unlocked_floors < 5: unlocked_floors += 1
                        break

                    # Attaque du Pokémon adverse
                    randomAttack = random.randint(1, 3)
                    if randomAttack == 1:
                        wildPokemonAttack = Pa("Rugissement", 0)
                        playerPokemon.power = max(1, playerPokemon.power - 2)
                        print(f"{wildPokemon.name} utilise {wildPokemonAttack.attack} !")
                    else:
                        wildPokemonAttack = Pa("Morsure", 7)
                        playerPokemon.lifePoint -= wildPokemonAttack.power
                        print(f"{playerPokemon.name} perd {wildPokemonAttack.power} LP")
                    if playerPokemon.lifePoint <= 0:
                        endFight = True
                        print(f"{wildPokemon.name} a battu {playerPokemon.name} !")

    # ========================
    # ARÈNE DE CÉLADÓPOLE
    # ========================
    if roads == 3:
        print("Bienvenue dans l'arène de Céladopole !")
        unlocked_floors = 1
        while True:
            print("Sélectionnez l'étage :")
            for f in range(1, min(unlocked_floors+1, 4)):
                name = "Premier" if f==1 else "Deuxième" if f==2 else "Troisième" if f==3 else "Quatrième" if f==4 else "Cinquième"
                print(f"{f}. {name} étage")
            floor_choice = int(input("Numéro de l'étage : "))

            if floor_choice <= unlocked_floors:
                if floor_choice == 1: wildPokemon = Wp("Herbizarre", "7 Lvl", "50 LP", "Plant", "8")
                elif floor_choice == 2: wildPokemon = Wp("Rafflesia", "8 Lvl", "55 LP", "Plant", "9")
                elif floor_choice == 3: wildPokemon = Wp("Joliflor", "9 Lvl", "60 LP", "Plant", "10")
                elif floor_choice == 4: wildPokemon = Wp("Mystherbe", "9 Lvl", "60 LP", "Plant", "10")
                elif floor_choice == 5: wildPokemon = Wp("Bulbizarre", "9 Lvl", "60 LP", "Plant", "10")
                print(f"Un dresseur vous défie avec {wildPokemon.name} !")

                playerPokemon = arrayTeamPokemon[0]
                endFight = False
                while not endFight:
                    print("Choisissez une attaque : 1.Griffe 2.Rugissement 3.Équipe 4.Sac")
                    pokemonFight = int(input("Numéro de l'attaque: "))

                    if pokemonFight == 1:
                        pokemonAttack = Pa("Griffe", 10)
                        wildPokemon.lifePoint -= pokemonAttack.power
                        print(f"{playerPokemon.name} utilise {pokemonAttack.attack} ! {wildPokemon.name} perd {pokemonAttack.power} LP !")
                    elif pokemonFight == 2:
                        pokemonAttack = Pa("Rugissement", 0)
                        wildPokemon.power = max(1, wildPokemon.power - 2)
                        print(f"{playerPokemon.name} utilise {pokemonAttack.attack} ! {wildPokemon.name} voit son attaque baisser à {wildPokemon.power} !")
                    elif pokemonFight == 3:
                        print("Choisissez un Pokémon:")
                        for i, pt in enumerate(arrayTeamPokemon):
                            print(f"{i+1}. {pt.name} {pt.level} {pt.lifePoint} {pt.type} {pt.power}")
                        arrayTeamPokemons = int(input("Numéro du Pokémon: "))
                        if 1 <= arrayTeamPokemons <= len(arrayTeamPokemon):
                            selectedPokemon = arrayTeamPokemon[arrayTeamPokemons - 1]
                            if selectedPokemon.lifePoint > 0:
                                playerPokemon = selectedPokemon
                                print(f"{playerPokemon.name} entre en scène !")
                            else:
                                print(f"{selectedPokemon.name} est K.O et ne peut pas combattre !")
                    elif pokemonFight == 4:
                        print("Choisissez un objet :")
                        for i, obj in enumerate(arrayBag):
                            print(f"{i+1}. {obj.object} x{obj.quantity}")
                        arrayBagObject = int(input("Numéro de l'objet: "))
                        if arrayBagObject == 2 and potion.quantity > 0:
                            potion.quantity -= 1
                            playerPokemon.lifePoint += 35
                            print(f"{playerPokemon.name} récupère {playerPokemon.lifePoint} LP")

                    if wildPokemon.lifePoint <= 0:
                        endFight = True
                        print(f"{playerPokemon.name} a battu {wildPokemon.name} !")
                        if unlocked_floors < 3: unlocked_floors += 1
                        break

                    randomAttack = random.randint(1, 3)
                    if randomAttack == 1:
                        wildPokemonAttack = Pa("Rugissement", 0)
                        playerPokemon.power = max(1, playerPokemon.power - 2)
                        print(f"{wildPokemon.name} utilise {wildPokemonAttack.attack} !")
                    else:
                        wildPokemonAttack = Pa("Morsure", 7)
                        playerPokemon.lifePoint -= wildPokemonAttack.power
                        print(f"{playerPokemon.name} perd {wildPokemonAttack.power} LP")
                    if playerPokemon.lifePoint <= 0:
                        endFight = True
                        print(f"{wildPokemon.name} a battu {playerPokemon.name} !")

    # ========================
    # ARÈNE DE CRAMOIS'ÎLE
    # ========================
    if roads == 4:
        print("Bienvenue dans l'arène de Cramois'Île !")
        unlocked_floors = 1
        while True:
            print("Sélectionnez l'étage :")
            for f in range(1, min(unlocked_floors+1, 4)):
                name = "Premier" if f==1 else "Deuxième" if f==2 else "Troisième"
                print(f"{f}. {name} étage")
            floor_choice = int(input("Numéro de l'étage : "))

            if floor_choice <= unlocked_floors:
                if floor_choice == 1: wildPokemon = Wp("Salamèche", "8 Lvl", "50 LP", "Fire", "9")
                elif floor_choice == 2: wildPokemon = Wp("Reptincel", "9 Lvl", "55 LP", "Fire", "10")
                elif floor_choice == 3: wildPokemon = Wp("Dracaufeu", "10 Lvl", "60 LP", "Fire", "12")
                elif floor_choice == 4: wildPokemon = Wp("Caninos", "10 Lvl", "60 LP", "Fire", "12")
                elif floor_choice == 5: wildPokemon = Wp("Feunard", "10 Lvl", "60 LP", "Fire", "12")
                print(f"Un dresseur vous défie avec {wildPokemon.name} !")

                playerPokemon = arrayTeamPokemon[0]
                endFight = False
                while not endFight:
                    print("Choisissez une attaque : 1.Griffe 2.Rugissement 3.Équipe 4.Sac")
                    pokemonFight = int(input("Numéro de l'attaque: "))

                    if pokemonFight == 1:
                        pokemonAttack = Pa("Griffe", 10)
                        wildPokemon.lifePoint -= pokemonAttack.power
                        print(f"{playerPokemon.name} utilise {pokemonAttack.attack} ! {wildPokemon.name} perd {pokemonAttack.power} LP !")
                    elif pokemonFight == 2:
                        pokemonAttack = Pa("Rugissement", 0)
                        wildPokemon.power = max(1, wildPokemon.power - 2)
                        print(f"{playerPokemon.name} utilise {pokemonAttack.attack} ! {wildPokemon.name} voit son attaque baisser à {wildPokemon.power} !")
                    elif pokemonFight == 3:
                        print("Choisissez un Pokémon:")
                        for i, pt in enumerate(arrayTeamPokemon):
                            print(f"{i+1}. {pt.name} {pt.level} {pt.lifePoint} {pt.type} {pt.power}")
                        arrayTeamPokemons = int(input("Numéro du Pokémon: "))
                        if 1 <= arrayTeamPokemons <= len(arrayTeamPokemon):
                            selectedPokemon = arrayTeamPokemon[arrayTeamPokemons - 1]
                            if selectedPokemon.lifePoint > 0:
                                playerPokemon = selectedPokemon
                                print(f"{playerPokemon.name} entre en scène !")
                            else:
                                print(f"{selectedPokemon.name} est K.O et ne peut pas combattre !")
                    elif pokemonFight == 4:
                        print("Choisissez un objet :")
                        for i, obj in enumerate(arrayBag):
                            print(f"{i+1}. {obj.object} x{obj.quantity}")
                        arrayBagObject = int(input("Numéro de l'objet: "))
                        if arrayBagObject == 2 and potion.quantity > 0:
                            potion.quantity -= 1
                            playerPokemon.lifePoint += 35
                            print(f"{playerPokemon.name} récupère {playerPokemon.lifePoint} LP")

                    if wildPokemon.lifePoint <= 0:
                        endFight = True
                        print(f"{playerPokemon.name} a battu {wildPokemon.name} !")
                        if unlocked_floors < 3: unlocked_floors += 1
                        break

                    randomAttack = random.randint(1, 3)
                    if randomAttack == 1:
                        wildPokemonAttack = Pa("Rugissement", 0)
                        playerPokemon.power = max(1, playerPokemon.power - 2)
                        print(f"{wildPokemon.name} utilise {wildPokemonAttack.attack} !")
                    else:
                        wildPokemonAttack = Pa("Morsure", 7)
                        playerPokemon.lifePoint -= wildPokemonAttack.power
                        print(f"{playerPokemon.name} perd {wildPokemonAttack.power} LP")
                    if playerPokemon.lifePoint <= 0:
                        endFight = True
                        print(f"{wildPokemon.name} a battu {playerPokemon.name} !")
