import math

value = 4.35

print(math.floor(value))
print(math.ceil(value))
print(round(value))

# round rounds 0.5 to even numbers so 4.5
# goes to 4 and 5.5 goes to 6
print(round(4.5))
print(round(5.5))

print(round(4.6))
print(round(5.4))

print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)

# Numpy is a library specifically designed for
# numerical processing. It goes much deeper than
# python's built in math module.

print(math.log(math.e))

print(math.log(100, 10))

print(math.sin(10))

print(math.degrees(math.pi / 2))

print(math.radians(180))

import random

print(random.randint(0, 100))

random.seed(101)
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))

my_list = list(range(0, 20))

print(my_list)
print(random.choice(my_list))

# Sample with replacement
print(random.choices(population=my_list, k=10))

# Sample without replacement
print(random.sample(population=my_list, k=10))

random.shuffle(my_list)
print(my_list)

print(random.uniform(a=0, b=100))
print(random.gauss(mu=0, sigma=1))