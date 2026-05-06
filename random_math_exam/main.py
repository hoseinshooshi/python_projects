import random
import time

operators = ["+", "-", "*"]; 
min_Operand = 3
max_operand = 12
total_problems = 5
user_score = 0

def generate_problem(): 
    left = random.randint(min_Operand, max_operand)
    right = random.randint(min_Operand, max_operand)
    operator = random.choice(operators)
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

expr, answer = generate_problem()

start = input("press Enter to Start: ")
start_time = time.time()
print("-----------------------")

for i in range(total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem number" + str(i+1) + ": " + expr + "= ")
        if guess == str(answer): 
            user_score += 1
            print("That was correct nicely done!")
            break
        else: 
            print("That was Wrong!")
            break
end_time = time.time()
user_time = round(end_time - start_time, 2)
print("-----------------------")
print("You have ended the Challange!!\nyour scoore is: " + str(user_score) + "/5\nand you have ended tha challange in",user_time ,"seconds")
print("-----------------------")