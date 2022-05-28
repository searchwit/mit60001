def total_savings(init_annual_salary, semi_annual_raise, portion_saved, r):
    annual_salary = init_annual_salary
    current_savings = 0
    for num_month in range(0, 36):
        if num_month > 0 and num_month % 6 == 0:
            # print(num_month)
            annual_salary = annual_salary * (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12
        current_savings = current_savings + monthly_salary * portion_saved + current_savings * r / 12

    return current_savings


def steps_best_savings(annual_salary):
    total_cost = 1000000
    semi_annual_raise = 0.07
    portion_down_payment = total_cost * 0.25
    r = 0.04
    portion_saved = 1  # change this value will affect the num_steps.
    low_portion = 0
    high_portion = 1
    current_savings = total_savings(annual_salary, semi_annual_raise, portion_saved, r)
    if current_savings < (portion_down_payment-100):
        print("starting salary: " + str(annual_salary))
        print("maximum savings (with saving rate =1) : " + str(current_savings))
        print("not afford")
        return -1
    num_step = 1
    while abs(current_savings - portion_down_payment) > 100:
        if current_savings > portion_down_payment:
            high_portion = portion_saved
            portion_saved = (portion_saved + low_portion)/2

        else:
            low_portion = portion_saved
            portion_saved = (portion_saved + high_portion)/2

        current_savings = total_savings(annual_salary, semi_annual_raise, portion_saved, r)
        num_step = num_step + 1

    print("starting salary: " + str(annual_salary))
    print("best saving rate: " + str(portion_saved))
    print("num of step: " + str(num_step))
    return num_step


steps_best_savings(10000)
steps_best_savings(150000)
