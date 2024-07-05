def select_players():
    print("TIC*TAC*TOE*")
    try: 
        players = int(input("Press 1 for a one-player game, or 2 for a two-player game: "))
        if players not in (1, 2):
            raise Exception
        return players
    except: 
        print("Invalid input. Defaulting to a one-player game")
        players = 1
        return players