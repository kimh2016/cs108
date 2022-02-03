"""CS 108 Lab 3.1

Make 4 prompts for any numbers
Make the last outcome sorted from minimum to maximum without using lst.sort() or sorted(lst).

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""

number_1 = float(input('number: '))
number_2 = float(input('number: '))
number_3 = float(input('number: '))
number_4 = float(input('number: '))
total = [number_1, number_2, number_3, number_4]
a = min(total)
total.remove(a)
b = min(total)
total.remove(b)
c = min(total)
total.remove(c)
d = min(total)
q = [a, b, c, d]
print(q)


             
