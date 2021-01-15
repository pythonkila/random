# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
25 - May -2020
"""


total_cost = int(input('Enter the cost of your dream house:$'))
annual_salary = int(input('Enter your annual salary:$'))
monthly_salary = round(annual_salary / 12)
portion_down_payment = round(0.25 * total_cost)
portion_saved = 0.15
savings = round(( monthly_salary * portion_saved))
current_savings = 0
rate = 0.04/12                      # Bank's monthly savings interest rate
month_counts = 0
# annual_return = current_savings*rate/12

while portion_down_payment > current_savings:
    current_savings += ( monthly_salary * portion_saved)
    current_savings = current_savings * ( 1 + rate)
    month_counts += 1
print("Your monthly salary is", str(monthly_salary) + "cad and you safe",savings,"monthly" )
print('You will need to safe for',month_counts,'months before you can afford down payment for your dream house')