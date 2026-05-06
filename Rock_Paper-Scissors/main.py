# play with the pc and track who won the most
import random 

user_wins = 0 
comp_wins = 0

options = ["rock", "paper", "scissors"]
# another way is to check user_pick == pc_pick as an elif for draw and else for the lost instead of the extended version written down blow, you can also remove the continue under the if and elif and also you can remove the pc_pick printer in body of the every if and elif and move it to the top of the if bodies

# consider this an exercise
while True: 
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()

    if user_input == "q":
        quit()
    if user_input not in options: 
        continue
    
    pc_number = random.randint(0,2)
    # rock=0, paper=1 , scissors=2
    pc_pick = options[pc_number]
    
    if user_input == "rock" and pc_pick == 'scissors':
        print("computer picked:", pc_pick)
        print("you won!")
        user_wins += 1
        print("Scores: ", "computer=",comp_wins, ", you=" ,user_wins)
        continue
    elif user_input == "rock" and pc_pick == 'paper':
        print("computer picked:", pc_pick)
        print("you lost!")
        comp_wins += 1
        print("Scores: ", "computer=",comp_wins, ", you=" ,user_wins)
        continue
    elif user_input == "rock" and pc_pick == 'rock':
        print("computer picked:", pc_pick)
        print("its a draw!")
        print("Scores: ", "computer=",comp_wins, ", you=" ,user_wins)
        continue
    elif user_input == "paper" and pc_pick == 'paper':
        print("computer picked:", pc_pick)
        print("its a draw!")
        print("Scores: ", "computer=",comp_wins, ", you=" ,user_wins)
        continue
    elif user_input == "scissors" and pc_pick == 'scissors':
        print("computer picked:", pc_pick)
        print("its a draw!")
        print("Scores: ", "computer=",comp_wins, ", you=" ,user_wins)
        continue
    elif user_input == "paper" and pc_pick == 'rock':
        print("computer picked:", pc_pick)
        print("you won!")
        user_wins += 1
        print("Scores: ", "computer=",comp_wins, ", you=" ,user_wins)
        continue
    elif user_input == "paper" and pc_pick == 'scissors':
        print("computer picked:", pc_pick)
        print("you lost!")
        comp_wins += 1
        print("Scores: ", "computer=",comp_wins, ", you=" ,user_wins)
        continue
    elif user_input == "scissors" and pc_pick == 'paper':
        print("computer picked:", pc_pick)
        print("you won!")
        user_wins += 1
        print("Scores: ", "computer=",comp_wins, ", you=" ,user_wins)
        continue
    elif user_input == "scissors" and pc_pick == 'rock':
        print("computer picked:", pc_pick)
        print("you lost!")
        comp_wins += 1
        print("Scores: ", "computer=",comp_wins, ", you=" ,user_wins)
        continue
    