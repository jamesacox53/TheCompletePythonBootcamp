my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    print(num)

for num in my_list:
    print("Hello")

for num in my_list:
    if ((num % 2) == 0):
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum = 0

for num in my_list:
    list_sum = list_sum + num

print(list_sum)

my_string = 'Hello World'

for letter in my_string:
    print(letter)

for _ in 'Hello World!':
    print('Hello')

tup = (1, 2, 3)

for item in tup:
    print(item)

my_list2 = [(1, 2), (3, 4), (5, 6), (7, 8)]

for (a, b) in my_list2:
    print(a)
    print(b)

for (a, b) in my_list2:
    print(a)

for (a, b) in my_list2:
    print(b)

my_list3 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for (a, b, c) in my_list3:
    print(b)

d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:
    print(item)

for item in d.items():
    print(item)

for (key, value) in d.items():
    print(value)

for value in d.values():
    print(value)