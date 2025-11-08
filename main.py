from function_choice_pokemon_trainer import choicePokemonTrainer as Cpt
from function_difficulty_mode import function_difficulty_mode as Fdm
from function_road import function_roads as Fr
from function_choice_pokemon import function_choice_pokemon as Fcp
from function_roads import function_grass as Fg
from bag import Bag as Bg

print(" === Bienvenue dans le monde des Pokémon ! ===\n")

while True:
    try:
        gameStart = int(input("Commencer la partie ? (1=Oui / 0=Non) "))
        if gameStart == 0:
            print("A bientôt, futur dresseur !")
            exit()
        elif gameStart == 1:
            break  # on sort de la boucle pour continuer le jeu
        else:
            print("Veuillez entrer 1 pour commencer ou 0 pour quitter.")
    except ValueError:
        print("Erreur : vous devez entrer un nombre (0 ou 1).")

arrayTeamPokemon = []

trainer_name = Cpt()
difficulty_mode = Fdm()

arrayBag = []

print(f"Je suis {trainer_name}, dresseur de Pokémon en route vers la ligue régionale de Kanto, prêt à prouver ma valeur et à devenir le meilleur !")
print("Je dois me rendre chez le professeur CHEN obtenir mon premier Pokémon.\n")

print("Sélectionnez le chemin dont vous souhaitez vous rendre")
print("1.Chez professeur CHEN")

road = Fr()

print("Bonjour Professeur CHEN, je viens pour obtenir mon premier pokémon")   
print(f"Bonjour {trainer_name}, tu arrives au bon moment. Tu as le choix entre ces trois pokémon")
print("Sélectionez le pokémon dont vous souhaitez voir les statistiques")
arrayTeamPokemon = Fcp()
pokeBall = Bg (f"pokeball", "", 5)
potion = Bg (f"potion", "35 Lp", 5)

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

    arenes = {
        2: { "name": "Azuria", "pokemon": [
                ("Otaria", 8, "50 LP", "Water", "7"),
                ("Poissirène", 9, "55 LP", "Water", "7"),
                ("Amonistar", 10, "60 LP", "Water", "8"),
                ("Têtarte", 11, "65 LP", "Water", "9"),
                ("Lokhlass", 12, "70 LP", "Water", "10")
            ],
            "max_floors": 5
        },
        3: { "name": "Céladopole", "pokemon": [
                ("Herbizarre", 7, "50 LP", "Plant", "8"),
                ("Rafflesia", 8, "55 LP", "Plant", "9"),
                ("Joliflor", 9, "60 LP", "Plant", "10"),
                ("Mystherbe", 9, "60 LP", "Plant", "10"),
                ("Bulbizarre", 9, "60 LP", "Plant", "10")
            ],
            "max_floors": 5
        },
        4: { "name": "Cramois'Île", "pokemon": [
                ("Salamèche", 8, "50 LP", "Fire", "9"),
                ("Reptincel", 9, "55 LP", "Fire", "10"),
                ("Dracaufeu", 10, "60 LP", "Fire", "12"),
                ("Caninos", 10, "60 LP", "Fire", "12"),
                ("Feunard", 10, "60 LP", "Fire", "12")
            ],
            "max_floors": 3
        }
    }
    
    roads = Fg(arrayTeamPokemon, arrayBag, arenes)
    Fg(arrayTeamPokemon, arrayBag, arenes)

   