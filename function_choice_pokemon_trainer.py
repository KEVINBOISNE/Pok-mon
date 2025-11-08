from pokemon_trainer import PokemonTrainer as Train

def choicePokemonTrainer():
    print("=== Sélectionnez votre dresseur Pokémon : ===")
    print("1. Sacha")
    print("2. Pierre")
    print("3. Ondine")

    while True:
        try:
            select = int(input("Entrez le numéro de votre choix (1-3) ou 0 pour quitter : "))

            if select == 0:
                print("A bientôt, futur dresseur !")
                exit()
            elif select == 1:
                trainer_name = Train("Sacha")
            elif select == 2:
                trainer_name = Train("Pierre")
            elif select == 3:
                trainer_name = Train("Ondine")
            else:
                print("Erreur : veuillez entrer un nombre entre 0 et 3.")
                continue  # revient au début de la boucle

            # Si on arrive ici, le choix est valide
            print(f"Vous avez sélectionné {trainer_name}")
            return trainer_name

        except ValueError:
            print("Erreur : vous devez entrer un nombre entier.")
