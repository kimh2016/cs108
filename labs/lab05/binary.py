"""CS 108 Lab 5.1

Write a program that takes in a positive integer as input,
and outputs a string of 1's and 0's representing the integer
in reversed binary. 

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""
#Make a program that can repeat as long as x is greater than 0.

x = int(input('integer: '))
str1 = ''

#use the while loop to iteratively divide by 2.

while x > 0 :
    out = x % 2  #remainder is 0 or 1. 
    str1 += str(out) #store the remainder in str1.
    x = x// 2 
print(str1)
