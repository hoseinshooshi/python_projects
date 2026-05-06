# generate a random number and calculate how many guesses it takes till the user gets it

import random
# second parameter in range doesnt come to generation
# if there is no first parameter by default it is considered 0
# if instead of randrange(first_para, second_para) you use randint(first_para, second_para) it will include the second_para too but you need to write the first_para too
# ask the user the second number
top_range = input("what would be the biggest number?")
# the int will turn string into number
if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("Type a Number bigger Than 0")
        quit()
else: 
    print("please type a number")
    quit()
random_number =  random.randrange(0,top_range)

# ask the user to guess the number
# this while loop continues when the conditions are reversed if you write user_guess != random_number as soon as user guesses the number the loop will break but here we wanna use and learn the break keyword that exits the loop while its line of code is executed
# the continue will bring us to the top of the loop
try_count = 0
while True: 
    try_count += 1
    user_guess = input("what do you think the number is?")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print("please type a number")
        continue
    
    if user_guess == random_number:
        print("you guessed the correct number on the", try_count  , "try")
        break
    elif user_guess > random_number: 
        print("the number is smaller!")
    else:
        print("the number is bigger")