def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))

def func_two(n):
    return list(map(str, range(n)))

print(func_two(10))

import time

def print_elapsed_time(func_name, func, arg):
    # Get current time before we run code
    start_time = time.time()

    # Run code
    result = func(arg)

    # Get current time after we run code
    end_time = time.time()

    # Get difference to calculate elapsed time
    elapsed_time = end_time - start_time
    print(f"The Elapsed Time for {func_name} in seconds: {elapsed_time}")

print_elapsed_time("func_one", func_one, 1000000)
print_elapsed_time("func_two", func_two, 1000000)

import timeit

setup1 = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

stmt1 = '''
func_one(100)
'''

print(timeit.timeit(stmt1, setup1, number=1000000))

setup2 = '''
def func_two(n):
    return list(map(str, range(n)))
'''

stmt2 = '''
func_two(100)
'''

print(timeit.timeit(stmt2, setup2, number=1000000))