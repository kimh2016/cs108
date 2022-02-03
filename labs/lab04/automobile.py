"""CS 108 Lab 4.0 

Write a program that prompts the user for an
automobile service. Output the user's input back out
and then output the price of the requested service.

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""

#first, make an input for the user.

service_request = input('service: ')
service_cost = 0

#Although if and elif statements work as well,
# if statements are okay too since the
# prices are set already.

if service_request == 'oil change' :
    service_cost = 35
if service_request == 'tire rotation' :
    service_cost = 19
if service_request == 'car wash' :
    service_cost = 7 

if service_cost == 0 :
    print('error:', service_request, 'is not recognized')
    
else :
    print('cost of', service_request + ': $' + str(service_cost))
