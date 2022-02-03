"""CS 108 - Lab 8.1

This module implements image processing functions using the Python Imaging
Library (PIL) to load and display images, and NumPy to manipulate the image's
2D array of pixels. Each pixel is represented as a list of intensity values
for red, green and blue (RGB), each value between 0 (low intensity) and 255 (
high intensity). For example:
    [0, 0, 0] represents black
    [255, 255, 255] represents white
    [255, 0, 0] represents red
Continued from lab 8, construct a function that blurs the image. 

@author:Hansol Kim (hk94) 
        Keith VanderLinden (kvlinden) and Ken Arnold (ka37)
@date: Spring, 2021
"""


from PIL import Image
import numpy as np
from copy import deepcopy


def load_image(filename):
    """ This function loads an image from the specified file. """

    # Convert pixel values to integer format in order to
    # allow arithmetic that may overflow np's default uint8.
    return np.array(Image.open(filename), dtype='int32')


def display_image(image_array):
    """ This function displays the given image. """

    # Convert pixel values from int back into uint8 for display.
    Image.fromarray(np.uint8(np.clip(image_array, 0, 255))).show()



def change_brightness(image, num):

    # Increase each RGB pixel value.
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            rgb = image[x][y]
            image[x][y] = [
                rgb[0] + num,
                rgb[1] + num,
                rgb[2] + num
            ]
    return image




def flip_horizontal(image):
    """ This function mirrors the given image around a vertical line. """

    # Why is this operation needed?
    # If I call the original image as image1, then let it equal to
    # image2 which is image_copy. Then use the image_copy to
    # flip the original image then return the original image.
    # If there was no deepcopy, the copy image is changed when the original
    # image is changed. The deepcopy makes it so that when you change the image,
    # image copy does not change. 
    image_copy = deepcopy(image)

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x][y] = image_copy[x][image.shape[1] - y - 1]

    return image

def flip_vertical(image):
    image_copy = deepcopy(image)
    
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x][y] = image_copy[image.shape[0] - x - 1][y]
            
    return image

def change_negative(image):
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            rgb = image[x][y]
            image[x][y] = [
                255 - rgb[0],
                255 - rgb[1],
                255 - rgb[2]
            ]

    return image

def greyscale(image):
    for x in range(image.shape[0]):
        for y in range(image.shape[1]): 
            rgb = image[x][y]
            image[x][y] = [
                (rgb[0] + rgb[1] + rgb[2])/3,
                (rgb[0] + rgb[1] + rgb[2])/3,
                (rgb[0] + rgb[1] + rgb[2])/3
                ]
    return image


def blur(image):
    """ Find the average of each of the color; red, green, blue.
        The blurfactor would be 1/9 since the pixel would be 3 by 3.
        First, assign the size of the image using the variable
        row and colum. Then use the loop to go over each matrix."""
    row = len(image)
    column = len(image[0])
    for x in range(1, len(image)-1):
        for y in range(1, len(image[x])-1):
            rgb = image[x][y]
            # Divide each color by 9 which will give the average of the matrix.
            # This means, to blur the image, average the ones that are adjacent
            # to a centered number. Thus, right and left, and up and down of the
            # centered number. Continue this for each red, green, and blue. 
            avg_r = (image[x-1][y-1][0] + image[x-1][y][0] + image[x-1][y+1][0] +
                     image[x][y-1][0] + image[x][y][0] + image[x][y+1][0] +
                     image[x+1][y-1][0] + image[x+1][y][0] + image[x+1][y+1][0])/9
            avg_g = (image[x-1][y-1][1] + image[x-1][y][1] + image[x-1][y+1][1] +
                     image[x][y-1][1] + image[x][y][1] + image[x][y+1][1] +
                     image[x+1][y-1][1] + image[x+1][y][1] + image[x+1][y+1][1])/9
            avg_b = (image[x-1][y-1][2] + image[x-1][y][2] + image[x-1][y+1][2] +
                     image[x][y-1][2] + image[x][y][2] + image[x][y+1][2] +
                     image[x+1][y-1][2] + image[x+1][y][2] + image[x+1][y+1][2])/9
            image[x][y] = [avg_r, avg_g, avg_b] # Now the average for rows and colums are complete.
            
    return image # This function is now ready to use in cli.py 












