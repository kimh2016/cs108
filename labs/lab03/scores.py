"""CS 108 Lab 3.3

Modify Sally's score as 13 and delete Tom's score from the dictionary.

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""

score_dict = {'Joe' : 10, 'Tom' : 23, 'Barb' : 13, 'Sue' : 19, 'Sally' : 12}
print(score_dict['Barb'])
score_dict['Sally'] = 13
del score_dict['Tom']
print(score_dict)

