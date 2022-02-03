""" CS 108 L Lab 2.0

Explain the expressiosn below and create a legal prompt.

@author: Hansol Kim (hk94)
@date: Spring 2021
"""

# Four rule calculation applies to python,
# which means multiplication, division are
# calculated first, then the addition and subtraction.

# 3 + 4 will simply be calculated as 7.

# 2 + 3 * 5 will calculate 3 * 5 first, then addition of 2, thus 17.

# 8 - 4 - 2, so 8 is subtracted from 4 and then 2 is 2.

# (3 + 7) * 2, numbers in parenthesis are calculated first, then times 2 is 20.

# 13 % 4, modulo operator evaluates the remainder of the division of the two integer operands
#thus, 13 / 4 is 3 and 1/4, but it will only output the remainder of 1. 

# 8.2 // 4, the floored division operator //
# can be used to round down the result of a
# floating-point division to the closest whole number value
# thus, the result would come out as 2.0

# 2**10, ** means the power of a number,
# so it would be calculated as 2 to the power of 10, it would come out as 1024

# 5.1 % 2, modulo operator evaluates the remainder of
# the division of the two integer operands, thus remainderwould be 1.1

# A user should be able to put any Number after 'Please enter an integer:'
# Number is a legal Python name, but 2_Number is not a legal name because
# it starts with a number 2.

Number = int(input('Please enter an integer: '))
