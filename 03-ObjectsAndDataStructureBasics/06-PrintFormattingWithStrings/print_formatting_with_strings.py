print('This is a string {}'.format('INSERTED'))

print('The {} {} {}'.format('fox', 'brown', 'quick'))

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))

print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

print('The {q} {q} {q}'.format(f='fox', b='brown', q='quick'))

result = 100/777

print("The result was {}".format(result))

print("The result was {r:1.3f}".format(r=result))

print("The result was {r:10.5f}".format(r=result))

result = 104.12345

print("The result was {r:1.3f}".format(r=result))

name = 'James'

print(f'Hello, his name is {name}')

name = 'Sam'
age = 3.14159

print(f'{name} is {age} years old!')

print(f'{name} is {age:10.3f} years old!')