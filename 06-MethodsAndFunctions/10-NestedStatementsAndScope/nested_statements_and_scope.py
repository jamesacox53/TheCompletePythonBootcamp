x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

# GLOBAL
name = 'This is a Global string'

def greet():
    # ENCLOSING
    name = 'Sammy'

    def hello():
        print('Hello ' + name)
    
    hello()

greet()
print(name)

def greet2():
    # ENCLOSING
    #name = 'Sammy'

    def hello():
        print('Hello ' + name)
    
    hello()

greet2()

def greet3():
    # ENCLOSING
    name = 'Sammy'

    def hello():
        # LOCAL
        name = 'John'
        
        print('Hello ' + name)
    
    hello()

greet3()

x = 50

def func(x):
    print(f'X is {x}')

func(40)
print(x)

def func2(x):
    print(f'X is {x}')

    x = 200
    print(f'I just locally changed x to {x}')

func2(45)
print(x)

def func3():
    # The global keyword tells python to go to the
    # Global namespace and grab that variable so we can
    # change it. In general avoid using the global keyword
    # unless absolutely necessary. Me: You can reassign a global
    # variable by returning the updated value from a function
    # and updating the global variable in the global scope.
    global x
    
    print(f'X is {x}')

    # local reassignment on a Global variable. So it will
    # affect the global x
    x = 200
    print(f'I just locally changed x to {x}')

func3()
print(x)