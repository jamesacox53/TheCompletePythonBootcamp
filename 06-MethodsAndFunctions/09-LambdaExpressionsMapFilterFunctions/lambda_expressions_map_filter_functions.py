def square(num):
    return num ** 2

my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

squared_nums = list(map(square, my_nums))
print(squared_nums)

def splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'EVEN'
    else:
        return my_string[0]
    
my_names = ['Andy', 'Eve', 'Sally']
spliced_names = list(map(splicer, my_names))
print(spliced_names)

def check_even(num):
    return num % 2 == 0

even_nums = list(filter(check_even, my_nums))
print(even_nums)

# The square(num) function as a lambda expression:
lambda num: num ** 2

# You can assign the anonymous function to a variable:
square2 = lambda num: num ** 2
print(square2(5))

squared_nums2 = list(map(lambda num: num ** 2, my_nums))
print(squared_nums2)

even_nums2 = list(filter(lambda num: num % 2 == 0, my_nums))
print(even_nums2)

first_letters_list = list(map(lambda name: name[0], my_names))
print(first_letters_list)