print("Welcome to the Game")

playing = input("Do you Wanna Play?(y/n) ")
user_score = 0
if playing.lower() != 'y':
    quit()

print("Okay! Lets Play")

answer = input("What is 2+2? ")
if answer == '4': 
    user_score += 1
    print("good job; your score now is ", user_score)
    
    continuing = input("Do you Wanna continue?(y/n) ")
    if continuing != 'y':
        print("see you later")
        quit()
else: 
    print("That was Wrong; your score now is:", user_score)

answer = input("What is 2+3? ")
if answer == '5': 
    user_score += 1
    print("good job; your score now is ", user_score)
    continuing = input("Do you Wanna continue?(y/n) ")
    if continuing != 'y':
        print("see you later")
        quit()
else: 
    print("That was Wrong; your score now is:", user_score)

print("You got ", user_score , " questions correct")