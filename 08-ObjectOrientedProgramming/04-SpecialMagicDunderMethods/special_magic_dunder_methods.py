# There are some special methods that allow us to use some
# built in operations in Python such as the len() function
# or the print() function with out own user created objects.
# This is where those special methods come into play. Special
# methods some people also call them Magic methods or Dunder
# methods because the use double underscores (__).
# 
# There are more special methods then the ones the instructor
# will show but for now theses are all we need. __init__ is
# the first special method we learned about and it's special
# because it's basically called automatically when you create
# the object.

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

my_book = Book('Python rocks', 'Jose', 200)

# When you call the print function of a Book it asks what is
# the string representation of my_book. So if we passed my_book
# into str(my_book) to cast it to a string what do we get.
# We can use the special method related to the string call
# __str__(self).
#
# If there's any function that asks for the string representation
# of an object then it's going to return what the __str__(self)
# method returns.
print("Book: ")
print(str(my_book))
print(my_book)


class Book2():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

my_book2 = Book2('Python rocks', 'Jose', 200)

print("")
print("Book2: ")
print(str(my_book2))
print(my_book2)


class Book3():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # The special method for len() is __len__(self)
    def __len__(self):
        return self.pages

my_book3 = Book3('Python rocks', 'Jose', 200)

print("")
print("Book3: ")
print(str(my_book3))
print(my_book3)
print(f"Length of Book3: {len(my_book3)}")


class Book4():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    # When you want to delete an object you can use
    # the keyword del. This is the special method for del.
    # Sometimes you might want other things to occur when you
    # delete a variable.
    def __del__(self):
        print("A boook object has been deleted")

my_book4 = Book4('Python rocks', 'Jose', 200)

print("")
print("Book4: ")
print(str(my_book4))
print(my_book4)
print(f"Length of Book4: {len(my_book4)}")
del my_book4