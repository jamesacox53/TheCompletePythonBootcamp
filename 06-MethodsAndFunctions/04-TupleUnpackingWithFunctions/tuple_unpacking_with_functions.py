stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

for (ticker, price) in stock_prices:
    print(ticker)

work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]

def employee_check(work_hours):
    """
    Returns the employee who has worked the most hours and the amount of
    hours they worked as a tuple.
    """

    current_max = 0
    employee_of_month = ''

    for (employee, hours) in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee

    return (employee_of_month, current_max)

print(employee_check(work_hours))
    
work_hours2 = [('Abby', 100), ('Billy', 4000), ('Cassie', 800)]

(name, hours) = employee_check(work_hours2)

print(f'Name: {name}, Hours: {hours}')