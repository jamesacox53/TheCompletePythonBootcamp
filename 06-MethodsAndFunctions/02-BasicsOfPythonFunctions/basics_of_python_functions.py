def say_hello():
    print("Hello")
    print("how")
    print("are")
    print("you")

say_hello()

def say_hello2(name="Default"):
    print(f"Hello {name}")

say_hello2("James")
say_hello2()

def add_num(num1, num2):
    return num1 + num2

result = add_num(10, 20)
print(result)

def print_result(a, b):
    print(a + b)

def return_result(a, b):
    return a + b

print_result(11, 21)

print(return_result(12, 22))

def sum_numbers(num1, num2):
    return num1 + num2

print(sum_numbers('10', '20'))