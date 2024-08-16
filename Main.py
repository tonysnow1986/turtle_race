import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_wager = screen.textinput(title="Place your wager", prompt="Which color turtle will win? ")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
y_pos = [-50, -30, -10, 10, 30, 50]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_wager:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 225:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_wager:
                print(f"Winner Winner!! The {winner} turtle is the winner!")
            else:
                print(f"You lose!!! The {winner} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
