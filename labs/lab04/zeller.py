"""CS 108 Lab 4.2

Make inputs for the user: year, month, day
and make the ouput as the day of the user's input. 

@author: Hansol Kim (hk94)
@date: Spring, 2021

"""
#I made inputs; year, month, and day.
#After that, I made another if else statement
#so that 13 and 14 input would be recognized
# as January and February minus one year.

year = int(input('Enter year: '))
month = int(input('Enter month: '))
day_of_month = int(input('Enter day: '))

if(month ==1) :
    month = 13
    year = year - 1
    
elif(month ==2) :
    month = 14
    year = year - 1
y,m,q = year, month, day_of_month

j = year // 100
k = year % 100
h = (q + ((26*(m + 1)) // 10) + k + (k // 4 ) + (j // 4) + 5*j) % 7

#I made a list of the days so whatever h is, it will be idicating
# the index order of the list I made. 
my_list_of_days = ['Saturday', 'Sunday', 'Monday', 'Tuesday',
     'Wednesday', 'Thursday', 'Friday'
     ]
print(my_list_of_days[h])


