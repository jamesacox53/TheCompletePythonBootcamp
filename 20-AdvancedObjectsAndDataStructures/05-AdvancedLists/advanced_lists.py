l = [1, 2, 3]

l.append(4)

print(l)

print(l.count(10))

print(l.count(1))

x = [1, 2, 3]

x.append([4, 5])

print(x)

x = [1, 2, 3]
x.extend([4, 5])

print(x)

print(l.index(2))

try:
    print(l.index(14))
except:
    print("Not in list")

print(l)

l.insert(2, 'Inserted')

print(l)

print(l.pop())

print(l)

print(l.pop(0))

print(l)

l.remove('Inserted')

print(l)

l = [1, 2, 3, 4, 3]

l.remove(3)

print(l)

l.reverse()

print(l)

l.sort()

print(l)