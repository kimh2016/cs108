"""CS 108 Lab 4.1

Make inputs for the temperature and wind speed.
The measurement should be invalid if the temperature
is below -58 or above 41, and wind speed cannot be lower
than 2mph. Lastly, if the wc_temp comes out as certain
number, make output as stay home, one layer, two layer, three layer,
and four layer accordingly. 


@author: Hansol Kim (hk94)
@date: Spring, 2021
"""

#First of all, since the formula is going to be used, import math.
#Then make inputs for the user.

import math
ta = float(input(('Temperature: ')))
v = float(input(('Wind speed: ')))

wc_temp = 35.74 + 0.6215*(ta) - 35.75*math.pow(v, 0.16) + 0.4275*(ta)*math.pow(v, 0.16)

#I made a variable for an if stament.
#I put the print('invalid input') as my priority
#then created otherwise if statements under the else statement
# so that invalid input and the layers woudln't come out together. 

no = (v < 2) or (ta < -58) or (ta > 41)

if no :
    print('Invalid input')
else:
    print('Wind chill:', wc_temp)
    if (wc_temp < -40) :
        print('Stay home!')
    elif (-40 <= wc_temp < -10) :
        print('Four layers')
    elif (-10 <= wc_temp < 20) :
        print('Three layers')
    elif (20 <= wc_temp < 40) :
        print('Two layers')
    elif (wc_temp >= 40) :
        print('One layer')