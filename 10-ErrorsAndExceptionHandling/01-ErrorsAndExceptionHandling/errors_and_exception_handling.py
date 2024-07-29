def add(n1, n2):
    print(n1 + n2)

add(10, 20)

number1 = 10
number2 = '20'

#add(number1, number2)

try:
    add(10, 10)
    # add(number1, number2)

except:
    print("Hey, it looks like you aren't adding correctly.")

else:
    # Block of code to run if there isn't an error.
    print("Add went well")


try:
    # f = open('testfile.txt', 'w')
    f = open('testfile.txt', 'r')
    # We should get an OSError error when we try to
    # write to a file we opened in read-only.
    f.write("Write a test line")

except TypeError:
    # You can specifically except for different types
    # of errors.
    print("There was a type error!")

except OSError:
    # On my work laptop I don't have permission to read or write.
    # So this except runs when I try to read or write.
    print("Hey you have an OS Error")

except:
    print("All other exceptions")

finally:
    print("I always run")


def ask_for_int():
    try:
        result = int(input("Please provide number: "))
    except:
        print("Whoops! That's not a number")
    finally:
        print("End of try/except/finally")

#ask_for_int()

def ask_for_int2():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That's not a number")
            continue
        else:
            print("Yes, thank you")
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end!")

ask_for_int2()