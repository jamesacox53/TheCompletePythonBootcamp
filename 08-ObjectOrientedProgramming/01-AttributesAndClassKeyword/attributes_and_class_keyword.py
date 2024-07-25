class Sample():
    # __init__ will be called whenever you create an
    # instance of the class
    def __init__(self):
        pass

my_sample = Sample()
print(type(my_sample))

class Dog():
    def __init__(self, breed):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed

my_dog = Dog(breed='Lab')
print(type(my_dog))
print(my_dog.breed)

# A way that should hopefully show better what is going on
class Dog2():
    def __init__(self, mybreed):
        self.breed = mybreed

my_dog2 = Dog2(mybreed='Huskie')
print(type(my_dog2))
print(my_dog2.breed)

class Dog3():
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots

my_dog3 = Dog3(breed='Lab', name='Sammy', spots=False)
print(type(my_dog3))
print(my_dog3.breed)
print(my_dog3.name)
print(my_dog3.spots)
