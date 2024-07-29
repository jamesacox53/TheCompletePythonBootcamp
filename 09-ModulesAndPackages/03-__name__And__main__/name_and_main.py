# When you start looking at larger .py scripts that you haven't
# written yourself you often see at the very bottom the line:
# if __name__ == "__main__":
# Then there's a block of code to be executed.

# Sometimes the whole idea behind that line of code is
# that when you are importing from a module you
# would like to know whether a modules function is 
# being used as an import, or if you are using the
# original .py file of that module.

# We will create 2 simple .py scripts and try to show
# the idea behind that if __name__ == "__main__": block
# of code that is usually at the end of larger .py script
# files. 

# Let's think about what actually happens when you call
# a python script at your command line. You go to your
# command line, and you type python space
# 'The name of your script .py'. what's actually happening
# when you call python myscript.py all of the code that's
# at indentation level zero is going to get run. That would
# mean that your functions, which are automatically usually going
# to be defined at indentation level zero and your classes also
# at indentation level zero are all going to be defined.

# Unlike other languages, in Python there's no main() function that
# you call somewhere at the top of your script that gets run
# automatically. Instead, what happens is: just implicitly, all
# the code at this indentation level zero gets run when you call
# the script file.

# in Python there is actually a built-in variable called __name__.
# So, just like there's built-in functions, this is a built-in
# variable, and it's quite obvious that it's built-in because
# we have two sets of double underscores in the beginning and
# in the back of it.

# What happens is this variable, __name__, gets assigned a string
# depending on how you're running the actual script. And if you run
# the script directly, so if I went to the command line and I wrote
# out python space one.py, what Python is going to do is going to
# assign this built-in variable called __name__ to be equal to
# "__main__". So Python does this in the background. It assigns
# the "__main__" string to the __name__ variable when you run
# it directly. That allows you to have an if block to check
# if they're equal to each other.

# So often what you do is something like this: You say,
# if __name__ == "__main": and then you can do something
# because you know that this particular .py file is being
# run directly, and if you ever run something directly in Python,
# you know this case happens to be true.

# So what happens is often people will just at the very bottom
# of their code, they'll say, if__name__ == "__main__" and
# then they say, kind of run a bunch of functions that they
# defined here. So at top they do a bunch of function definitions.
# Then all the way at the bottom, they actually organize their code
# on what they actually want to execute. And they know that they
# wanna execute it because they say if this built-in variable
# called __name__ happens to be equal to the string "__main__"
# then I know I'm running this .py file directly.

# Typically, people will define a bunch of functions and classes
# at the top of the file and then have the 
# if __name__ == "__main__": block to execute the code they want
# to run when the file is run directly.