def even_check(number):
    return number % 2 == 0

def check_even_list(num_list):
    """
    Return True if any number is even inside a list.
    """
    for number in num_list:
        if even_check(number):
            return True
        else:
            pass

    return False

print(check_even_list([1, 3, 5]))

print(check_even_list([2, 3, 5]))

print(check_even_list([2, 4, 5]))

print(check_even_list([1, 3, 6]))

def check_even_list2(num_list):
    """
    Return all numbers in the list that are even.
    """
    even_numbers = []

    for number in num_list:
        if even_check(number):
            even_numbers.append(number)

    return even_numbers

print(check_even_list2([1, 3, 5]))

print(check_even_list2([2, 3, 5]))

print(check_even_list2([2, 4, 5]))

print(check_even_list2([1, 3, 6]))