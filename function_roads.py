from roads import Roads as Rds
import random
from pokemon_attack import PokemonAttack as Pa
from pokemon_states import PokemonStates as Ps
from function_bag import use_item as UseItem
from function_arenes import arene as Arn

def function_grass(arrayTeamPokemon, arrayBag, arenes):
    """
    Fonction principale des routes et hautes herbes :
    - Permet au joueur de choisir où aller (hautes herbes ou arènes)
    - Lance les combats Pokémon sauvages dans les herbes
    - Appelle les arènes correspondantes
    """
    while True:
        print("\n=== Sélectionnez le chemin dont vous souhaitez vous rendre : ===")
        print("1. Dans les hautes herbes")
        print("2. Arène d'Azuria")
        print("3. Arène de Céladopole")
        print("4. Arène de Cramois'Île")
        print("0. Quitter ce menu")

        try:
            roads = int(input("Entrez le numéro de votre choix pour la sélection du chemin (1-4) ou 0 pour quitter : "))
        except ValueError:
            print("Erreur : veuillez entrer un nombre entre 0 et 4.")
            continue

        if roads == 0:
            print("A bientôt, futur dresseur !")
            exit()

        # === DANS LES HAUTES HERBES ===
        if roads == 1:
            print("Vous entrez dans les hautes herbes...")
            roadsOption = Rds("Dans les hautes herbes")
            print(roadsOption)

            while True:
                try:
                    print("\nUn Pokémon sauvage apparaît ! Souhaitez-vous le combattre ?")
                    print("1. Combattre")
                    print("2. Fuir")
                    meetingPokemon = int(input("Entrez le numéro de votre choix: "))
                    if meetingPokemon not in [1, 2]:
                        print("Veuillez entrer 1 pour combattre ou 2 pour fuir.")
                        continue
                    break
                except ValueError:
                    print("Erreur : vous devez entrer 1 ou 2.")

            if meetingPokemon == 1:
                playerPokemon = arrayTeamPokemon[0]
                wildPokemon = Ps("Rattata", "3 Lvl", "47 LP", "Normal", "7")
                endFight = False

                while not endFight:
                    try:
                        print("Choisissez une action : 1.Griffe 2.Rugissement 3.Équipe 4.Sac")
                        pokemonFight = int(input("Numéro de l'action: "))
                    except ValueError:
                        print("Erreur : vous devez entrer un nombre entre 1 et 4.")
                        continue

                    if pokemonFight == 1:
                        pokemonAttack = Pa("Griffe", 10)
                        wildPokemon.lifePoint -= pokemonAttack.power
                        print(f"{playerPokemon.name} utilise {pokemonAttack.attack} !")
                        print(f"{wildPokemon.name} perd {pokemonAttack.power} LP !")

                    elif pokemonFight == 2:
                        pokemonAttack = Pa("Rugissement", 0)
                        wildPokemon.power = max(1, wildPokemon.power - 2)
                        print(f"{playerPokemon.name} utilise {pokemonAttack.attack} !")
                        print(f"{wildPokemon.name} voit son attaque baisser à {wildPokemon.power} !")

                    elif pokemonFight == 3:
                        print("Choisissez un Pokémon :")
                        for i, pt in enumerate(arrayTeamPokemon):
                            print(f"{i+1}. {pt.name} {pt.level} {pt.lifePoint} {pt.type} {pt.power}")
                        try:
                            idx = int(input("Numéro du Pokémon: "))
                            if 1 <= idx <= len(arrayTeamPokemon):
                                selectedPokemon = arrayTeamPokemon[idx - 1]
                                if selectedPokemon.lifePoint > 0:
                                    playerPokemon = selectedPokemon
                                    print(f"{playerPokemon.name} entre en scène !")
                                else:
                                    print(f"{selectedPokemon.name} est K.O et ne peut pas combattre !")
                            else:
                                print("Numéro invalide.")
                                continue
                        except ValueError:
                            print("Erreur : vous devez entrer un nombre.")
                            continue

                    elif pokemonFight == 4:
                        UseItem(arrayBag, playerPokemon, wildPokemon, arrayTeamPokemon)

                    # Fin combat
                    if wildPokemon.lifePoint <= 0:
                        endFight = True
                        print(f"{playerPokemon.name} a battu {wildPokemon.name} !")
                        break

                    # Attaque du Pokémon sauvage
                    if random.randint(1, 3) == 1:
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

        # === ARÈNES ===
        elif roads in [2, 3, 4]:
            Arn(arrayTeamPokemon, arrayBag, arenes[roads])

        else:
            print("Choix invalide, entrez un nombre entre 0 et 4.")
