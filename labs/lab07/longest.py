"""CS 108 Lab 6.2

Desing an algorithm of a function to find the longest
string from a list using an accumulator pattern. 

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""
"""
def find_longest(some_list) :
    count = 0 # set count to 0
    for i in some_list : #Go through the whole list 
        if len(i) > count : #checking for the longest word(string) 
            count = len(i)
            word = i
        elif len(i) == 0 :
            return ''
    return word # return the string
"""

def find_longest(some_list) :
    if some_list == []: #if the list is empty, it returns '',
            return ''   # if not, the algorithm moves on to count
    count = 0 # set count to 0
    for i in some_list : #Go through the whole list 
        if len(i) > count : #checking for the longest word(string) 
            count = len(i)
            word = i
        elif len(i) == 0 : #this indicates that the list includes '' string
            return ''
    return word
    


