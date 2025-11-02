from difficulty_mode import DifficultyMode as Dm

def function_difficulty_mode():

    print("Choisiez la difficulté")
    print("1.Easy")
    print("2.Normal")
    print("3.Hard")
    while True:
            try:
                difficultyMode = int (input( "Entrez le numéro de votre choix pour la selection de la difficulté (1-3) ou 0 pour quitter :"))

                if difficultyMode == 0:
                    print("A bientôt, futur dresseur !")
                    exit()

                elif difficultyMode == 1:
                    difficultyOption = Dm("Easy")
                elif difficultyMode == 2:
                    difficultyOption = Dm("Normal")
                elif difficultyMode == 3:
                    difficultyOption = Dm("Hard")
                else:
                    print("Erreur : veuillez entrer un nombre entre 0 et 3.")
                    continue  # revient au début de la boucle

                # Si on arrive ici, le choix est valide
                print(difficultyOption)
                return difficultyOption
            
            except ValueError:
                print("Erreur : vous devez entrer un nombre entier.")
