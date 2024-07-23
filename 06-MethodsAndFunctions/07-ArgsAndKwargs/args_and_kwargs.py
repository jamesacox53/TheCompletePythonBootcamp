# With *args you can pass in as many arguments as you want
# and python will take all the parameters that are passed in
# and set them to be inside a tuple.
def myfunc(*args):
    return sum(args) * 0.05

print(myfunc(40, 60, 100, 1, 34))

# When an argument starts with a star term it says whatever
# this parameter is the user can pass in as many as they want
# and it's going to be treated as a tuple inside the function.
def myfunc2(*args):
    print(args)

myfunc2(40, 60, 100, 1, 34)

def myfunc3(*spam):
    print(spam)

myfunc3(40, 60, 100, 1, 34)

# **kwargs builds a dictionary of key value pairs.
def myfunc4(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("I didn't find any fruit here")

myfunc4(fruit='apple')

def myfunc5(**kwargs):
    print(kwargs)

myfunc5(fruit='apple', veggie='lettuce')

def myfunc6(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))

myfunc6(10, 20, 30, 40, fruit='orange', food='eggs', animal='dog')