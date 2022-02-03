"""CS 108 - Lab 8.1

This module runs a command-line interface that controls successive image
processing commands. The image is redisplayed after each command.

Continued from lab 8, construct a function that blurs the image.

@author:Hansol Kim (hk94) 
        Keith VanderLinden (kvlinden) and Ken Arnold (ka37)
@date: Spring, 2021
"""

from image_processing import *

#add menus accordingly

MENU = '\nb - blur' \
       '\nb+ - brighten' \
       '\nb- - dim' \
       '\nn - negative' \
       '\nfh - Flip Horizontal' \
       '\nfv - flip Vertical' \
       '\ng - greyscale' \
       '\nq - Quit' 

image = load_image('images/sydney_sunset.png')

# Run a CLI loop, allowing the user to repeat commands by hitting enter.
previous_command = ''
while True:
    display_image(image)
    print(MENU)
    command = input('Command: ').lower()

    if command == '':
        command = previous_command
    if command == 'b' :
        image == blur(image)
    if command == 'b+': #both b+ and b- would essentialy come from one function.
        image = change_brightness(image, num = 25)
    elif command == 'b-':
        image = change_brightness(image, num = -25)
    elif command == 'n': #changes image into negative image using 255 - rgb[0]
        image = change_negative(image)
    elif command == 'fh': #flip the image horizontally and vertically by changing x and y values. 
        image = flip_horizontal(image)
    elif command == 'fv':
        image == flip_vertical(image)
    elif command == 'g': #the sum of each rgb list divide three gives us the average (grey color) of the image.
        image == greyscale(image)
    elif command == 'q':
        break
    else:
        print('invalid command')

    previous_command = command
    