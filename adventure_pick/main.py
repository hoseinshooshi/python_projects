import random

user_name = input("What is your name?")
print("wlcome", user_name , "to this Adventure")

first_level_random = random.randint(0,1)

if first_level_random == 0: 
    answer = input("you are on a dirty cross road, do you wanna go left or right?(R/L) ").lower()
    if answer == 'l':
        answer = input("you have reached a river do you wanna swim or walk around it?(S/W)").lower()
        if answer == "s":
            print("the current was too much, you lost!")
            quit()
        elif answer == "w":
            answer = input("you reached a city, do you wanna enter the city?(Y/N)").lower
        else:
            print("not a valid option, you lost")
            quit()
    elif answer == 'r':
        print("the land was barren, you died!")
        quit()
    else:
        print("not a valid option, you lost")
        quit()
else: 
    answer = input("there is a sound coming from the bushes, you wanna check it or ignore it?(C/I) ").lower()
    if answer == "c": 
        print("you have been killed!!")
        quit()
    elif answer == "i":
        answer = input("there is a river nearby you wanna drink some water?(Y/N)")
        if answer == "y":
            answer = input("you are not thirsty now;you have reached a river do you wanna swim or walk around it?(S/W) ")
            print("..")
            if answer == "s":
                print("the current was too much, you lost!")
                quit()
            elif answer == "w":
                answer = input("you reached a city, do you wanna enter the city?(Y/N)").lower
            else:
                print("not a valid option, you lost")
                quit()
        elif answer == "n": 
            print("you died of thirst!")
            quit()
    else: 
        print("not a valid option, you lost!")
        quit()
