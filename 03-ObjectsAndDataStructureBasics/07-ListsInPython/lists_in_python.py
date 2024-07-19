my_list = [1, 2, 3, 4]
print(my_list)
print(len(my_list))


my_list2 = ['String', 1234, 55.345]
print(my_list2)
print(len(my_list2))

print(my_list[0])

print(my_list[1:])

my_list3 = my_list + my_list2
print(my_list3)

my_list3[0] = "ONE ALL CAPS"
print(my_list3)

my_list3.append('six')
print(my_list3)

my_list3.append('seven')
print(my_list3)

popped_item = my_list3.pop()
print(popped_item)
print(my_list3)

popped_item2 = my_list3.pop(0)
print(popped_item2)
print(my_list3)

alphabet_list = ['a', 'e', 'x', 'b', 'c']
alphabet_list.sort()
print(alphabet_list)

number_list = [4, 2, 7, 9, 1]
number_list.sort()
print(number_list)

alphabet_list.reverse()
print(alphabet_list)

number_list.reverse()
print(number_list)