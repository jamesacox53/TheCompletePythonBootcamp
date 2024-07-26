# Inheritance -------------------------------------------
print("Inheritance:")

class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

print("")
print("Animal: ")
my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()

class Dog(Animal):
    def __init__(self):
        # Me: I think you have to specificall call the __init__
        # constructor method of the parent class first or the constructor
        # function of the parent class doesn't run.
        Animal.__init__(self)

        print("Dog Created")

print("")
print("Dog: ")
my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()

class Dog2(Animal):
    def __init__(self):
        # If you don't call the __init__ constructor function of the parent
        # class then the __init__ constructor function of the parent class
        # doesn't run. But the child class still inherits the methods of the
        # parent class. The child class can still overwrite the methods of
        # the parent class.
        
        print("Dog2 Created")

    def who_am_i(self):
        print("I am a Dog2!")

print("")
print("Dog2: ")
my_dog2 = Dog2()
my_dog2.who_am_i()
my_dog2.eat()

class Dog3(Animal):
    def __init__(self):
        Animal.__init__(self)

        print("Dog3 Created")

    def who_am_i(self):
        print("I am a Dog3!")

print("")
print("Dog3: ")
my_dog3 = Dog3()
my_dog3.who_am_i()
my_dog3.eat()

class Dog4(Animal):
    def __init__(self):
        Animal.__init__(self)

        print("Dog4 Created")

    def who_am_i(self):
        print("I am a Dog4!")

    def eat(self):
        print("I am eating and I am a Dog4")

    # A child class can have it's own methods
    def bark(self):
        print("Woof")

print("")
print("Dog4: ")
my_dog4 = Dog4()
my_dog4.who_am_i()
my_dog4.eat()
my_dog4.bark()

# Polymorphism -------------------------------------------
print("")
print("-------------------------------------------")
print("Polymorphism:")

class Dog5():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"
    
class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"
    
niko = Dog5("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())

print("")
for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

# Abstract class - never expect to instantiate, this is
# only expected to serve as a Base class. Me: I guess we
# can't actually make it an abstract class but we just expect
# that it will never actually be created.
class Animal2():
    def __init__(self, name):
        self.name = name

        print("Animal2 Created!")

    def speak(self):
        # Raise an Error
        raise NotImplementedError("Subclass must implement this abstract method")
    
class Dog6(Animal2):
    def __init__(self, name):
        Animal2.__init__(self, name)

    def speak(self):
        return self.name + " says woof!"
    
class Cat2(Animal2):
    def __init__(self, name):
        Animal2.__init__(self, name)

    def speak(self):
        return self.name + " says meow!"

print("")
niko2 = Dog6("Niko2")
felix2 = Cat2("Felix2")
print(niko2.speak())
print(felix2.speak())