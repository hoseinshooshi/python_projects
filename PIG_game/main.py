import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)
    return roll

value = roll()

while True: 
    how_many_players = input("Enter the number of players:(2-4)(q for quit) ")
    if how_many_players.isdigit():
        how_many_players = int(how_many_players)
        if 1 < how_many_players <= 4:
            break
        else: 
            print("the minimum amount of players is 2 and the max amount is 4;" + "\n" "please try again")
            continue
    if how_many_players == 'q': 
        print("see you later!!")
        quit()
    else: 
        print("not a valid option, please try again!!")
        continue

max_score = random.randint(30, 143)
players_scores = [0 for _ in range(how_many_players)]

while max(players_scores) < max_score: 
    for players_i in range(players):   
        print("\n player", players_i + 1 , "turn has just started \n")
        dice_counter = 0
        current_score = 0
        while True:
            should_roll = input("do you wanns roll the dice?(y/n) ").lower()
            if should_roll != "y":
                break
            value = roll()
            if value == 1: 
                current_score = 0
                print("you rolled a 1! your turn is done")
                break
            else: 
                current_score += value
                print("you rolled:", value)

        players_scores[players_i] += current_score
        print("your score now is:", players_scores[players_i])