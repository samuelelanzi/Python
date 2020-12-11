import turtle

from random import *

wn = turtle.Screen()

turtlebase = turtle.Turtle() 
turtle1 = turtle.Turtle() 

turtle1.color("blue") 
turtle1.pencolor("blue") 

count = 0 
while count <= 2000: 
    turtle1.setheading(randint(0, 360)) 
    turtle1.forward(randint(-10, 10)) 
    count = count + 1

wn.mainloop ()