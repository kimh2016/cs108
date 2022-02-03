"""CS 108 Lab 5.0

Write a program whose input is two integers.
Make increments of 10 of the first integer to the second integer
as long as the first integer is less than or equal to the second
integer. Do not use a prompt for the input. 

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""
#first, make inputs for two integers.

integer = int(input())
integer2 = int(input())

#Create an if-else statement, but with another while statement
#within the else satement so that if the first integer is less
#than or equal to the second integer, it would proceed until it
#reaches the second integer.

if integer > integer2 :
    print("Second integer can't be less than the first.")
else :
    while integer <= integer2 :
        print(integer, end = '\n')
        integer += 10


