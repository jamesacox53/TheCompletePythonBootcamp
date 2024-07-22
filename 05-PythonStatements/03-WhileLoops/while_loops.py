x = 0

while (x < 5):
    print(f'The current value of x is {x}')

    x += 1
else:
    print('x is not less than 5')

y = 50

while (y < 5):
    print(f'The current value of y is {y}')

    y += 1
else:
    print('y is not less than 5')

z = [1, 2, 3]

for item in z:
    pass

my_string = 'Sammy'

for letter in my_string:
    if (letter == 'a'):
        continue
    
    print(letter)

for letter in my_string:
    if (letter == 'a'):
        break
    
    print(letter)

k = 0

while k < 5:
    if (k == 2):
        break

    print(k)
    k += 1