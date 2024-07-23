def myfunc(*args):
    sum = 0

    for arg in args:
        sum += arg

    return sum

print(myfunc(1, 2, 3, 4, 5, 6, 7))