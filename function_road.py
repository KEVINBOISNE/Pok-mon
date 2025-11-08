from roads import Roads as Rds
from function_choice_pokemon import function_choice_pokemon as Fcp

def function_roads():
    while True:
        try:
            roads = int(input("Entrez le numéro de votre choix pour la sélection du chemin 1 ou 0 pour quitter : "))

            if roads == 0:
                print("A bientôt, futur dresseur !")
                exit()

            # Chemin 1 : Professeur Chen
            elif roads == 1:
                roadsOption = Rds("Chez professeur CHEN")
            
            print(roadsOption)
            return roadsOption

        except ValueError:
            print("Erreur : vous devez entrer un nombre entier.")

