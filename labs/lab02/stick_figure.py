"""CS 108 - Lab 2.2

Draw a sick figure man by using the turtle pen.
Set a unit as 50.

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""

import turtle

window = turtle.Screen()
pen = turtle.Turtle()
import math

UNIT = 50
pen.circle(UNIT)
pen.right(90)
pen.forward(UNIT)
pen.right(90)
pen.forward(UNIT)
pen.backward(UNIT)
pen.backward(UNIT)
pen.forward(UNIT)
pen.left(90)
pen.forward(UNIT)
pen.right(45)
pen.forward(math.sqrt(UNIT**2 + UNIT**2))
pen.backward(math.sqrt(UNIT**2 + UNIT**2))
pen.left(90)
pen.forward(math.sqrt(UNIT**2 + UNIT**2))
pen.hideturtle()



# window.mainloop() # Needed for some IDEs.
