from pokemon_states import PokemonStates as Ps

def function_choice_pokemon():
    arrayTeamPokemon = []
    choiceConfirm = False

    while not choiceConfirm:
        print("\nChoisissez votre Pokémon :")
        print("1. Pikachu")
        print("2. Salamèche")
        print("3. Bulbizarre")
        print("4. Carapuce")
        print("0. Quitter le jeu")

        try:
            pokemonStatistics = int(input("Entrez le numéro de votre choix (0-4) : "))

            if pokemonStatistics == 0:
                print("A bientôt, futur dresseur !")
                exit()
            elif pokemonStatistics == 1:
                pokemonStats = Ps("Pikachu", "5 Lvl", "50 LP", "Electrik", "10")
            elif pokemonStatistics == 2:
                pokemonStats = Ps("Salamèche", "5 Lvl", "1000 LP", "Fire", "1000")
            elif pokemonStatistics == 3:
                pokemonStats = Ps("Bulbizarre", "5 Lvl", "55 LP", "Plant", "11")
            elif pokemonStatistics == 4:
                pokemonStats = Ps("Carapuce", "5 Lvl", "70 LP", "Water", "13")
            else:
                print("Erreur : veuillez entrer un nombre entre 0 et 4.")
                continue  # relance la saisie

            # Affichage des stats
            print(f"\nStatistiques du Pokémon choisi : {pokemonStats}")

            # Confirmation du choix
            print("Souhaitez-vous garder ce Pokémon ?")
            print("1. Oui")
            print("2. Non")
            keepPokemon = int(input("Entrez le numéro de votre choix : "))

            if keepPokemon == 1:
                choiceConfirm = True
                arrayTeamPokemon.append(pokemonStats)
                print(f"Parfait ! {pokemonStats.name} rejoint votre équipe !")
            elif keepPokemon == 2:
                print("Très bien, vous pourrez choisir un autre Pokémon plus tard.")
            else:
                print("Erreur : veuillez entrer 1 ou 2.")

        except ValueError:
            print("Erreur : vous devez entrer un nombre entier.")

    return arrayTeamPokemon
