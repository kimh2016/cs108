"""CS 108 Homework 2

Make two rectangles with output conditions like 'the rectangles overlap',
'the rectangle 1 contains rectangle 2' vice versa, and otherwise
'the rectangles are disjoint'. 

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""
from guizero import App, Drawing, Text

app = App('Drawing Canvas')
d = Drawing(app, width = 'fill', height = 'fill')

#first, make inputs for r1x,r1y,r1width,r1height, r2x,r2y,r2width, and r2height.

r1x = int(input('Enter rectangle 1 x: '))
r1y = int(input('Enter rectangle 1 y: '))
r1w = int(input('Enter rectangle 1 width : '))
r1h = int(input('Enter rectangle 1 height: '))
d.rectangle(r1x, r1y, r1w + r1x, r1h + r1y, color='white', outline=True)

r2x = int(input('Enter rectangle 2 x: '))
r2y = int(input('Enter rectangle 2 y: '))
r2w = int(input('Enter rectangle 2 width : '))
r2h = int(input('Enter rectangle 2 height: '))
d.rectangle(r2x, r2y, r2w + r2x, r2h + r2y, color='white', outline=True)

# I made a condition for the disjoint first, then used elif statement
#for the other two rectangles that contains one another no matter of
#the order. Then used else statement for the overlap chances.
#Using two elif statement came out to be the best solution for me to make
# much simpler calculation. 

if r1w < abs(r2x - r1x) or r1h < abs(r2y - r1y) or r2w < abs(r1x -r2x) or r2h < abs(r1y -r2y) :
    print('The rectangles are disjoint.')
    text = Text(app, text = 'The rectangles are disjoint.')
elif r2x > r1x and r2y - r1y and r1w + r1x > r2w +r2x and r1h + r1y > r2h + r2y  :
    print('Rectangle 1 contains rectangle 2.')
    text = Text(app, text = 'Rectangle 1 contains rectangle 2.')
elif r1x > r2x and r1y > r2y and r2w +r2w > r1w +r1x and r2h +r2h > r1h + r1h :
    print('Rectangle 2 contains rectangle 1.')
    text = Text(app, text = 'Rectangle 2 contains rectangle 1.')
else :
    print('The rectangles overlap.')
    text = Text(app, text = 'The rectangles overlap.')
    
#texts that appear on canvas works perfectly fine on guizero,
#but I don't know why zybook makes it wrong. 
