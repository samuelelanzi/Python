import turtle

from random import *

wn = turtle.Screen()

turtlebase = turtle.Turtle() 
c = turtle.Turtle() 

c.color("blue") 
c.pencolor("blue") 

i = 0 
while i != 2000: 
    c.setheading(randint(0, 360)) 
    c.forward(randint(-10, 10)) 
    i = i + 1

wn.mainloop ()