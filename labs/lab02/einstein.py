"""CS 108 - Lab 2.1 

Complete the Eistein Puzzle.
Any three digit integers in the prompt "Number: "
should come out as 1089

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""

# Put your solution code here, replacing this line.
import math
num = int(input('Number: '))
digit1 = num // 100
digit2 = (num % 100) // 10 
digit3 = num % 10
rev_number = digit3*100 + digit2*10 + digit1
difference = math.fabs(num - rev_number)
digitA = difference // 100
digitB = (difference % 100) // 10  
digitC = difference % 10
rev_diff = digitC*100 + digitB*10 +digitA
print(int(difference + rev_diff))



      
