"""CS 108 Homework 1

Draw a Netherlands flag using a turtle pen.
Then make an input for the user that can be
made to any size that is scale of 3 : 2. 

@author: Hansol Kim (hk94)
@date: Spring 2021
"""
import turtle
t = turtle
t.speed(-10)
t.setup(600, 400)

#Decide a starting position

t.penup()
t.goto((-100, 90))
t.pendown()

# Set UNIT_1 as 180.
# Set UNIT_2 at ratio of 3:2 of the UNIT_1.
# Thus UNIT_2 should be 120 but be divided by 3
# since there are three sections of colors in the flag.
UNIT_1 = 180
UNIT_2 = 120 / 3

#Determine the colors in the flag
#darkred = #AE1C28
#darkblue = #21468B

#We need to divide the box in 1 / 3
#First fill in the top box with dark red

t.color('#AE1C28')
t.begin_fill()
t.forward(UNIT_1)
t.right(90)
t.forward(UNIT_2)
t.right(90)
t.forward(UNIT_1)
t.end_fill()

#Start coloring the middle box with white
#Then draw a black line frame the white box

t.color('white')
t.begin_fill
t.left(90)
t.color('black')
t.forward(UNIT_2)

#Start coloring the bottom box with dark blue

t.color('#21468B')
t.begin_fill()
t.forward(UNIT_2)
t.left(90)
t.forward(UNIT_1)
t.left(90)
t.forward(UNIT_2)
t.end_fill()

#Finally draw a black line to frame the white box
#Hide the turtle

t.color('black')
t.forward(UNIT_2)
t.hideturtle()





