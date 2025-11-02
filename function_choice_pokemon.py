from pokemon_states import PokemonStates as Ps

def function_choice_pokemon():
    arrayTeamPokemon = []
    choiceConfirm = False
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
    return arrayTeamPokemon
