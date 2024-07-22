for num in range(10):
    print(num)

for num in range(3, 10):
    print(num)

for num in range(3, 10, 2):
    print(num)

my_list = list(range(0, 11, 2))
print(my_list)

index_count = 0

for letter in 'abcde':
    print(f'At index {index_count} the letter is {letter}')

    index_count += 1

word = 'xyz'

for (index, letter) in enumerate(word):
    print(f'At index {index} the letter is {letter}')

my_list1 = [1, 2, 3]
my_list2 = ['a', 'b', 'c']

for (elem1, elem2) in zip(my_list1, my_list2):
    print(f'{elem1}, {elem2}')

my_list3 = [1, 2, 3, 4, 5, 6, 7, 8]

for (elem3, elem2) in zip(my_list3, my_list2):
    print(f'{elem3}, {elem2}')

my_list4 = list(zip(my_list1, my_list2))
print(my_list4)

print('x' in [1, 2, 3])

print('x' in ['x', 'y', 'z'])

print('a' in 'a world')

d = {'myKey': 'myVal'}

print('myKey' in d.keys())

print('myVal' in d.values())

my_list5 = [10, 20, 30, 40, 100]

print(min(my_list5))

print(max(my_list5))

from random import shuffle

my_list6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

shuffle(my_list6)

print(my_list6)

from random import randint

my_num = randint(0, 100)

print(my_num)

user_num_str = input("Please enter a number here: ")
user_num = int(user_num_str)
print(user_num)