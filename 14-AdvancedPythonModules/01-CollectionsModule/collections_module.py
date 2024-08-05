# Counter is designed for us to count unique elements
from collections import Counter

my_list = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]

counter = Counter(my_list)
print(counter)

my_list2 = ['abc', 'abc', 'bc', 'bc', 'd']

counter2 = Counter(my_list2)
print(counter2)

counter3 = Counter("slfkgjsdlfkjbaoadfdsfaoivadijdb")
print(counter3)
print(counter3.most_common(1))

# Just get Unique Values
print(list(counter3))

# defaultdict assigns a default value if there's an instance
# where a key error would have occurred. If you try to ask for
# a key which doesn't exist in a defaultdict it will assign it
# with some default value.
from collections import defaultdict

d = {'a': 10}
print(d)
print(d['a'])
try:
    print(d['wrong'])
except:
    print("Key doesn't exist")

d2 = defaultdict(lambda: 0)

d2['correct'] = 100
print(d2['correct'])
print(d2['wrong'])
print(d2)

my_tuple = (10, 20, 30)
print(my_tuple[0])

from collections import namedtuple

# You created a named tuple like a class
Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sammy = Dog(age=5, breed='Husky', name='Sam')
print(type(sammy))
print(sammy)

# A namedtuple is kind of like a Tuple but now 
# there's an association with each value: age, breed,
# name. You can refer to these properties with the name
# or with the index.
print(sammy.age)
print(sammy.breed)
print(sammy.name)
print(sammy[0])
print(sammy[1])
print(sammy[2])