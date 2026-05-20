# turtle is a basic built in module that allows you to perform 2d graphic operas.
import turtle
import random
import time
# define screen size
WIDTH, HEIGHT = 480, 480
COLORS = ["cyan", "red", "green", "blue", "orange", "black", "yellow", "purple", "pink", "brown"]
def get_Number_Tutles():
    get_Number_Tutle = 0
    while True:
        get_Number_Tutle = input("How many Turtles you Wanna Race:(2-10) ")
        if get_Number_Tutle.isdigit():
            get_Number_Tutle = int(get_Number_Tutle)
            if 2<= get_Number_Tutle <=10:
                print(f"you will race with {get_Number_Tutle} turtles")
                return get_Number_Tutle
                break
            else:
                print("Enter a Number between 2-10")
                continue
        else:
            print("Please Enter a Valid Number between 0-10")
            continue
def init_turtle(): 
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing Game")
def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i+1) * spacing_x, -HEIGHT//2 + 30 )
        racer.pendown()
        turtles.append(racer)
    return turtles
def racing(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            x,y = racer.pos()
            if y >= HEIGHT//2-10:
                return colors[turtles.index(racer)]

get_Number_Tutle = get_Number_Tutles()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:get_Number_Tutle]
winner = racing(colors)
print(f"The '{winner}' Turtle has Won!!!")
time.sleep(5)
