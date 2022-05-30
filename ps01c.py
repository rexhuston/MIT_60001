# PS1 B
# Rex Huston
# 05/29/2022

# bi-section search
# use bi-section search to determin savings rate needed to achieve
# down payment after 36 months

# assumptions
semi_annual_raise = .07
investment_return = .04
house_price = 1000000
down_payment = .25 * house_price
months_to_save = 36
current_savings = 0

# desired precision is .01, meaning we can search between 0 and 10000.
# dividing that number by 100 will give us a number at hundredths
precision = 10000


#bi-section search variables
min = 0
max = 10000


# get salary from user
enter_salary = float(input("Enter your salary: "))



#guess counter
guess = 0

while abs(down_payment - current_savings) > 100 and (max-min)>1:
    #increment guess counter
    guess = guess + 1

    #reset current savings, salary and mid var
    current_savings = 0
    annual_salary = enter_salary
    monthly_salary = enter_salary/12
    mid = int((min + max) / 2)

    
    #calculate how much would be saved after 36 months
    for i in range(1, 37, 1):
        #increment monthly salary
        current_savings = current_savings * (1+investment_return/12) + (monthly_salary * (mid/precision))

        #every 6 months, apply semi-annual raise
        if i % 6 == 0:
            annual_salary = annual_salary*(1+semi_annual_raise)
            monthly_salary = annual_salary/12

    if current_savings > down_payment:
        max = mid
    else:
        min = mid
    
   
    
    

#outputs
if(max-min) > 1:
    print("Best savings rate: ", mid/precision)
    print("Number of guesses: ", guess)
else:
    print("it is not possible to pay the down payment in 3 years")
