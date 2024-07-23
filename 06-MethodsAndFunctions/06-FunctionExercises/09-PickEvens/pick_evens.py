def myfunc(*args):
    even_list = []

    for arg in args:
        if arg % 2 == 0:
            even_list.append(arg)

    return even_list

print(myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9))