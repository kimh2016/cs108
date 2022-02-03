"""CS 108 Lab 5.2

Create a spirograph using the given equation. Use while loops
to make repetitions of the next x and y. 

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""
#Use guizero for drawing and import math for the calculation of the equation.

from guizero import App, Drawing
import math
app = App('Drawing Canvas')
d = Drawing(app, width = 'fill', height = 'fill')

#Make prompts for the user that will be used in the equation.

r = float(input('moving radius: '))
R = float(input('fixed radius: '))
p = float(input('pen offset: '))
color = str(input('color: '))
center = app.width / 2

#Set the initial position (starting position).

x = (R + r) * math.cos(0) + p * math.cos(((R+r)*0/r)) + center
y = (R + r) * math.sin(0) + p * math.sin(((R+r)*0/r)) + center

#Make a while loop as t is incremented by 0.1 while t is less than 360.

t = 0
while t < 360 :
    t += 0.1
    next_x = (R + r) * math.cos(t) + p * math.cos(((R+r)*t/r)) + center
    next_y = (R + r) * math.sin(t) + p * math.sin(((R+r)*t/r)) + center
    d.line(x, y,
           next_x, next_y,
           color)
    x = next_x
    y = next_y 

