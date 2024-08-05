def create_cubes(n):
    result = []

    for x in range(n):
        result.append(x ** 3)

    return result

print("Cubes")
print(create_cubes(10))

def create_cubes2(n):
    for x in range(n):
        yield x ** 3

for x in create_cubes2(10):
    print(x)

print("\n------------------------")
print("Cubes2")
print(list(create_cubes2(10)))

def gen_fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        yield a
        
        temp_a = a
        a = b
        b = temp_a + b

print("\n------------------------")
print("Fibonacci")
for num in gen_fibonacci(10):
    print(num)

def simple_generator():
    for x in range(3):
        yield x

print("\n------------------------")
print("Simple Generator")
for num in simple_generator():
    print(num)

print("\n------------------------")
print("G - next")
g = simple_generator()
print(g)
# Me: You can only call next on a generator/iterator object.
print(next(g))
print(next(g))
print(next(g))

print("\n------------------------")
print("iter - normal for loop")
s = "hello"

for letter in s:
    print(letter)

print("\n------------------------")
print("iter - iter function")
# Me: To turn an object that is iterable into an iterator that we can
# iterate over we can use the iter function. Then we can call the next
# function on it.
s_iter = iter(s)
print(s_iter)
print(next(s_iter))
print(next(s_iter))