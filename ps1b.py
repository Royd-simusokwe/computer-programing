print("please enter the following:")

#this will enable the user o put there cost, annual salary and portion saved

total_cost = float(input("how much is your deam house  "))
annual_salary = float(input("annual salary  "))
portion_saved = float(input("portion_saved  "))
semi_annual_rise = float(input("semi annual rise  "))

#the following are the variables for all costs and amounts

current_savings = 0
portion_down_payment = 0.25 * total_cost
r = 0.04
portion_saved= portion_saved*(annual_salary/12)
months_to_be_covered = 0

while current_savings <= portion_down_payment:
    months_to_be_covered +=1
    current_savings += (current_savings*r/12) + portion_saved

    if months_to_be_covered % 6 ==0:
        annual_salary += annual_salary * semi_annual_rise
        monthly_saved = (annual_salary/12) * portion_saved
        
print("you will purchase the house after " + str(months_to_be_covered) + " months of saving")
