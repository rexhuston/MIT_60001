# PS1 B
# Rex Huston
# 05/29/2022

# Description
# Gather info from User
# Calculate in months how long to save down payment
# Same as 1A, but with a semi-annual raise

# Definitions
# total_cost - cost of dream home
# portion_down_payment - decimal, percentage portion of 
#   cost needed for down payment. .25 = 25%
# current_savings - the amount I have saved so far
# r - annual rate of return
# annual_salary - amount I earn per year
# monthly_salary = annual_salary / 12
# portian_saved - decimal, savings rate. eg .10 = 10% of annual salary saved
# semi_annual_raise - decimal, percentage raise every 6 months.

# set constants
portion_down_payment = .25
r = .04

# ask the user for: annual salary, portion of salary to be saved, cost of dream home
annual_salary = float(input("Please enter your annual salary: "))
portion_saved = float(input("What portion of your salary are you saving? "))
total_cost = float(input("What is the price of your dream home? "))
semi_annual_raise = float(input("What is the semi-annual raise? "))

months = 0
monthly_salary = annual_salary / 12
current_savings = 0
down_payment = portion_down_payment * total_cost


while current_savings < down_payment:
    #increase current savings by return on investment + this months portion saved
    current_savings = (current_savings*(1+r/12)) + (monthly_salary*portion_saved)
    months = months + 1

    #check if time for raise, calculate new salary and reset monthly salary
    if months %6 == 0:
        annual_salary = annual_salary*(1+semi_annual_raise)
        monthly_salary = annual_salary / 12
   

print("Number of Months: ", months)