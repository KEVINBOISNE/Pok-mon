from function_bag import function_bag as Fb, use_item as UseItem
from pokemon_attack import PokemonAttack as Pa
from pokemon_states import PokemonStates as Ps
import random

def arene(arrayTeamPokemon, arrayBag, arene):
    print(f"=== Bienvenue dans l'arène de {arene['name']} ! === ")
    unlocked_floors = 1

    while True:
        print("Sélectionnez l'étage :")
        print("0. Retour")
        for f in range(1, min(unlocked_floors + 1, arene["max_floors"] + 1)):
            names = ["Premier", "Deuxième", "Troisième", "Quatrième", "Cinquième"]
            print(f"{f}. {names[f-1]} étage")
        
        floor_choice = int(input("Numéro de l'étage : "))
        if floor_choice == 0:
            print("Retour")
            break
        
        if 1 <= floor_choice <= unlocked_floors:
            poke_info = arene["pokemon"][floor_choice - 1]
            wildPokemon = Ps(*poke_info)
            print(f"Un dresseur vous défie avec {wildPokemon.name} !")

            playerPokemon = arrayTeamPokemon[0]
            endFight = False

            while not endFight:
                print("Choisissez une attaque : 1.Griffe 2.Rugissement 3.Équipe 4.Sac")
                pokemonFight = int(input("Numéro de l'attaque: "))

                if pokemonFight == 1:
                    atk = Pa("Griffe", 10)
                    wildPokemon.lifePoint -= atk.power
                    print(f"{playerPokemon.name} utilise {atk.attack} ! {wildPokemon.name} perd {atk.power} LP !")
                elif pokemonFight == 2:
                    atk = Pa("Rugissement", 0)
                    wildPokemon.power = max(1, wildPokemon.power - 2)
                    print(f"{playerPokemon.name} utilise {atk.attack} ! {wildPokemon.name} voit son attaque baisser à {wildPokemon.power} !")
                elif pokemonFight == 3:
                    print("Choisissez un Pokémon :")
                    for i, pt in enumerate(arrayTeamPokemon):
                        print(f"{i+1}. {pt.name} {pt.level} {pt.lifePoint} {pt.type} {pt.power}")
                    idx = int(input("Numéro du Pokémon: "))
                    if 1 <= idx <= len(arrayTeamPokemon):
                        sel = arrayTeamPokemon[idx - 1]
                        if sel.lifePoint > 0:
                            playerPokemon = sel
                            print(f"{playerPokemon.name} entre en scène !")
                        else:
                            print(f"{sel.name} est K.O !")
                elif pokemonFight == 4:
                    UseItem(arrayBag, playerPokemon)

                # Fin combat
                if wildPokemon.lifePoint <= 0:
                    endFight = True
                    print(f"{playerPokemon.name} a battu {wildPokemon.name} !")
                    if unlocked_floors < arene["max_floors"]:
                        unlocked_floors += 1
                    break

                # Attaque du Pokémon adverse
                if random.randint(1,3) == 1:
                    atk = Pa("Rugissement", 0)
                    playerPokemon.power = max(1, playerPokemon.power - 2)
                    print(f"{wildPokemon.name} utilise {atk.attack} !")
                else:
                    atk = Pa("Morsure", 7)
                    playerPokemon.lifePoint -= atk.power
                    print(f"{playerPokemon.name} perd {atk.power} LP")
                
                if playerPokemon.lifePoint <= 0:
                    endFight = True
                    print(f"{wildPokemon.name} a battu {playerPokemon.name} !")
