"""CS 108 Lab 10.0

Modify the lists in the employees.txt, giving variables to each values of index. 

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""

from employee import Employee

# Load an employee object for each employee specified in 'employees.txt' into the employees list.
outfile = open("employees.txt", "r")
employees = [] # make an empty list 
for employee_line in outfile:
    value = employee_line.split(',')
    # Listing index
    given_name = value[0]
    family_name = value[1]
    rank = value[2]
    salary = int(value[3])
    individual = Employee(given_name, family_name, rank, salary)
    employees.append(individual)

employees_count = open("employee-count.txt", "w")
count = len(employees)
employees_count.write(str(count))
employees_count.close()

# Compute and print out statistics for employees

# Write the total number of employees into the 'employee-count.txt' file.

totals = {} # make dictionaries for totals and counts. 
counts = {}
max_employee = employees[0]
min_employee = employees[0]
for employee in employees:
    if employee.rank in totals:
        totals[employee.rank] += employee.salary
        counts[employee.rank] += 1
    else:
        totals[employee.rank] = employee.salary
        counts[employee.rank] = 1  
    if employee.salary > max_employee.salary:
        max_employee = employee
    if employee.salary < min_employee.salary:
        min_employee = employee

print('Maximum and Minimum Salaries')
print(str(max_employee))
print(str(min_employee))
print("Rank and Average Salaries")
for rank in totals:
    print(rank + ': {:.2f}'.format(totals[rank] / counts[rank]))

# for the last part of the lab, modify the previous lab to actually write
# the maximum, minium, rank, and average of the salaries into the text file. 
employee_stat = open('employee-stats.txt', 'w')
employee_stat.write('Maximum and Minimum Salaries'+'\n')
employee_stat.write(str(max_employee) + '\n')
employee_stat.write(str(min_employee) + '\n')
employee_stat.write("Rank and Average Salaries"'\n')
for rank in totals:
    employee_stat.write(rank + ': {:.2f}'.format(totals[rank] / counts[rank]) + '\n')
employee_stat.close()            
       
