from roads import Roads as Rds
from function_choice_pokemon import function_choice_pokemon as Fcp

def function_roads(arrayTeamPokemon):
    while True:
        try:
            roads = int(input("Entrez le numéro de votre choix pour la sélection du chemin (1-3) ou 0 pour quitter : "))

            if roads == 0:
                print("A bientôt, futur dresseur !")
                exit()

            # Chemin 1 : Professeur Chen
            elif roads == 1:
                roadsOption = Rds("Chez professeur CHEN")
            
            # Chemin 2 : Hautes herbes
            elif roads == 2:
                if not arrayTeamPokemon:  # si la liste est vide
                    print("Vous devez d'abord choisir un Pokémon avant d'aller dans les hautes herbes !")
                    continue
                roadsOption = Rds("Dans les hautes herbes")
            
            # Chemin 3 : Arène d'Azuria
            elif roads == 3:
                if not arrayTeamPokemon:
                    print("Vous devez d'abord choisir un Pokémon avant d'aller dans l'arène !")
                    continue
                roadsOption = Rds("Arène d'Azuria")

            else:
                print("Erreur : veuillez entrer un nombre entre 0 et 3.")
                continue

            print(roadsOption)
            return roadsOption

        except ValueError:
            print("Erreur : vous devez entrer un nombre entier.")

