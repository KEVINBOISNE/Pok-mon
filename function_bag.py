from bag import Bag as Bg
import random

def function_bag(arrayBag):
    for item in arrayBag:
        print(f" - {item.object} x{item.quantity}")
    return arrayBag


def use_item(arrayBag, playerPokemon, wildPokemon, arrayTeamPokemon):
    print("Choisissez un objet :")
    for i, obj in enumerate(arrayBag):
        print(f"{i+1}. {obj.object} x{obj.quantity}")

    try:
        choix = int(input("Numéro de l'objet: "))
        if not (1 <= choix <= len(arrayBag)):
            print("Choix invalide.")
            return
    except ValueError:
        print("Erreur : vous devez entrer un nombre.")
        return

    objet = arrayBag[choix - 1]

    # Potion
    if objet.object.lower() == "potion":
        if objet.quantity > 0:
            objet.quantity -= 1
            playerPokemon.lifePoint += 35
            print(f"{playerPokemon.name} récupère 35 LP ({playerPokemon.lifePoint} LP total).")
        else:
            print("Vous n'avez plus de potion ou pas de Pokémon à soigner !")

    # Pokéball
    elif objet.object.lower() == "pokeball":
        if objet.quantity > 0:
            objet.quantity -= 1
            print("Tu lances une Pokéball…")

            # Chance de capture = 50% + bonus si Pokémon faible
            capture_chance = 50
            roll = random.randint(1, 100)

            if roll <= capture_chance:
                print(f"Félicitations ! {wildPokemon.name} a été capturé !")
                arrayTeamPokemon.append(wildPokemon)
                # Le Pokémon sauvage n'est plus actif
                wildPokemon.lifePoint = 0
            else:
                print(f"Oh non ! {wildPokemon.name} a échappé à la capture…")
        else:
            print("Impossible de lancer la Pokéball ici.")

    else:
        print("Cet objet n'est plus disponible !")
