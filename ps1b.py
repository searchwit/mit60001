annual_salary = float(input("your annual salary: "))
portion_saved = float(input("percent to save: "))
total_cost = float(input("cost of home: "))

semi_annual_raise = float(input("semi annual raise: "))

portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12
num_month = 0
while current_savings < portion_down_payment:
    if num_month > 0 and num_month % 6 == 0:
        print(num_month)
        annual_salary = annual_salary * (1 + semi_annual_raise)
    monthly_salary = annual_salary / 12
    current_savings = current_savings + monthly_salary * portion_saved + current_savings * r/12
    num_month = num_month + 1


print("num of month: " + str(num_month))
