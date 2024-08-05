def func():
    return 1

print(func())

def hello():
    return "Hello!"

greet = hello

print(greet())

del hello

# greet is still pointing to the original function object.
# Functions are objects that can be passed into other objects.
print(greet())

def hello2(name="Jose"):
    print("The hello2() function has been executed!")

    def greet2():
        return "\t This is the greet2() function inside hello2!"
    
    def welcome2():
        return "\t This is welcome2() inside hello2"
    
    print(greet2())
    print(welcome2())
    print("This is then end of the hello2 function!")

hello2()

def hello3(name="Jose"):
    print("The hello3() function has been executed!")

    def greet3():
        return "\t This is the greet3() function inside hello3!"
    
    def welcome3():
        return "\t This is welcom3() inside hello3"
    
    print("I am going to return a function.")

    if name == "Jose":
        return greet3
    else:
        return welcome3
    
my_new_func = hello3("Jose")
print(my_new_func())

def cool():
    def super_cool():
        return "I am very cool!"
    
    return super_cool

some_func = cool()
print(some_func())

def hello4():
    return "Hi Jose!"

def other(some_def_func):
    print("Other code runs here!")
    print(some_def_func())

other(hello4)

def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the original function")
        
        original_func()

        print("Some extra code. after the original function!")

    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!!!")

decorated_func = new_decorator(func_needs_decorator)

decorated_func()

def new_decorator2(original_func):
    def wrap_func():
        print("Some extra code 2, before the original function")
        
        original_func()

        print("Some extra code 2. after the original function!")

    return wrap_func

@new_decorator2
def func2_needs_decorator():
    print("I want to be decorated2!!!")

func2_needs_decorator()