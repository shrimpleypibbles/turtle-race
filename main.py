from turtle import Turtle, Screen
import random


wn = Screen()
wn.setup(width=500, height=400)
user_bet = wn.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
speeds = [0, 10, 6, 3, 1]
turtles = {}
is_on = True

y_cord = -100
for i in colors:
    t = Turtle(shape="turtle")
    t.color(i)
   # t.speed(random.choice(speeds))
    t.penup()
    t.goto(x=-230, y=y_cord)
    y_cord += 40

    turtles[i[0]] = t

while is_on:
    for value in turtles.values():
        x_pos = value.pos()[0]
        if x_pos == 200:
            winner = value.color()[0]
            print(f"The winner is {value.color()[0]}")
            is_on = False
        elif x_pos != 200:
            value.forward(random.randint(1, 11))
if user_bet == winner:
    print("You won!")
else:
    print("You lost!")


















wn.exitonclick()
