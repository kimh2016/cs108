"""CS 108 Lab 6.3

Write a function named count_unique_words
that collects and returnsthe unique words
in the text. 

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""
# Make a function that will be used in the second function.

def search(unique_words, current_word) :
    for i in range(len(unique_words)) :
        if current_word == unique_words[i] :
            return i # returns the current word
    return -1 #if the value is -1, it goes to the second function. 
    
def count_unique_words(str_list) :
    unique_words = [] #unique words contain all unique words
    for s in str_list : #for each string in string list
        if search(unique_words, s) == -1 : # if not in unique words append string
            unique_words.append(s)
            
    return unique_words #return unique words

#print(count_unique_words(['i', 'i', 'i'])) returns ['i']