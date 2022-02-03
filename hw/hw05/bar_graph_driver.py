"""CS 108 Homework 5 

In this homework, upgrade the bar graph implementation
that is built in a previous homework. Base this code 
on the solution to the previous homework assignment.
create a separate module, bar_graph_driver.py that
imports the BarGraph class and tries it out.

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""


# Pull out guizero and import drawing.
from guizero import App, Drawing 
from bar_graph import BarGraph # Call bar_graph module as well as BarGraph class.
import random # Import random for random colors.

# Set the canvas size.
app = App('Drawing Canvas')
height = 500
width = 500
drawing = Drawing(app, width = 500, height = 500)

filename = input('Filename: ') # The user inputs the name of the text file.
outfile = open(filename, 'r') # Opens the file and reads the text file

l = [] # In a empty list, append the list from the text file.
for i in outfile:
    l.append(i.strip()) # Get rid of whitespaces.
    
integer = [] # From l, we need to separate the string and the integers
for i in l[1:]:
    integer.append(int(i))

color = l[0] # The first index in l is a string, and the rest are integers. 
bg = BarGraph(integer, color) # Imports BarGraph class 
bg.draw(drawing, app.width, app.height)
# print(bg) #Prints out the string that represents the graph. 

















