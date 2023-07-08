import turtle
from turtle import Screen
import time
from random import randint

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Turtle Catching Game")

turtle_instance = turtle.Turtle()
turtle_instance.color("green")
turtle_instance.shape("turtle")

turtle_instance.hideturtle()
screen = Screen()

score = 0

score_board = turtle.Turtle()
score_board.hideturtle()
score_board.penup()
score_board.goto(-50, 250)
score_board.write("Your score: {}".format(score), font=("Arial", 15, "normal"))

def sol_tik(x, y):
    global score
    if turtle_instance.distance(x, y) < 20:
        score += 1
        score_board.clear()
        score_board.write("Your score: {}".format(score), font=("Arial", 15, "normal"))

drawing_board.onscreenclick(sol_tik)


countdown = 15
countdown_turtle = turtle.Turtle()
countdown_turtle.hideturtle()
countdown_turtle.penup()
countdown_turtle.goto(-50, 220)
countdown_turtle.write("Countdown: {}".format(countdown), font=("Arial", 15, "normal"))

for i in range(countdown):
    countdown -= 1
    time.sleep(1)
    countdown_turtle.clear()
    countdown_turtle.write("Countdown: {}".format(countdown), font=("Arial", 15, "normal"))


    turtle_instance.shape('turtle')
    turtle_instance.penup()
    turtle_instance.hideturtle()
    turtle_instance.goto(randint(-300, 300), randint(-280, 280))
    turtle_instance.showturtle()

turtle_instance.hideturtle()
countdown_turtle.clear()
countdown_turtle.goto(-80,0)
countdown_turtle.write("Game Over",font=("Arial",30,"normal"))



turtle.mainloop()