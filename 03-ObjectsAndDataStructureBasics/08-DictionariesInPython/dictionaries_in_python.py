my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)

print(my_dict['key1'])

prices_lookup = { 'apple': 2.99, 'oranges': 1.99, 'milk': 5.80 }
print(prices_lookup['apple'])

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': { 'insideKey': 100 }}

print(d['k2'])
print(d['k3']['insideKey'])

print(d['k2'][2])

d2 = { 'key1': ['a', 'b', 'c'] }
print(d2['key1'][2].upper())

d3 = { 'k1': 100, 'k2': 200 }
d3['k3'] = 300
print(d3)

d3['k1'] = 'New Value'
print(d3)

print(d3.keys())
print(d3.values())
print(d3.items())