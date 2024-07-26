class Dog():
    # Class Object Attribute - These are the same for
    # any instance of a class
    species = 'mammal'
    
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots

my_dog = Dog(breed='Lab', name='Sammy', spots=False)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)

class Dog2():
    species = 'mammal'
    
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # Operations/Actions -> Methods. They look like
    # functions in a class. A method is a function
    # inside of a class that will work with the object
    # in some way.
    def bark(self, number):
        print("Woof! My name is {} and the number is {}".format(self.name, number))

my_dog2 = Dog2('Lab', 'Frankie')
print(type(my_dog2))
print(my_dog2.breed)
print(my_dog2.name)
print(my_dog2.species)

my_dog2.bark(15)

class Circle():
    pi = 3.14159

    def __init__(self, radius=1):
        self.radius = radius

        # Can create attribute
        self.area = self.pi * (radius ** 2)

        # Can call Class attribute with either self (self.pi) 
        # or with the name of the Class (Circle.pi)
        # self.area = Circle.pi * (radius ** 2)

    def get_circumference(self):
        return self.radius * self.pi * 2
    
my_circle = Circle()
print("")
print("my_circle:")
print(f"Pi: {my_circle.pi}")
print(f"Radius: {my_circle.radius}")
print(f"Area: {my_circle.area}")
print(f"Circumference: {my_circle.get_circumference()}")

my_circle2 = Circle(30)
print("")
print("my_circle2:")
print(f"Pi: {my_circle2.pi}")
print(f"Radius: {my_circle2.radius}")
print(f"Area: {my_circle2.area}")
print(f"Circumference: {my_circle2.get_circumference()}")