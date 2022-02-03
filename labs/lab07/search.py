"""CS 108 Lab 6.1

Write a linear search function named search that searches for a target in a
list of elements, returning the position of the first occurrence of the target
in the list. If it doesn't find the target, it returns -1.

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""
str_list = ['this', 'is', 'the', 'day']
target = 'is'

# Make a function that finds the target from the str_list.

def search(str_list, target) : 
    for i in range(len(str_list)) : #starting from the first one. 
        if target == str_list[i] :
            return i # returns the target if found in the str_list.
    return -1 # returns -1 if target not found in the str_list. 

# print(search(str_list,target))

