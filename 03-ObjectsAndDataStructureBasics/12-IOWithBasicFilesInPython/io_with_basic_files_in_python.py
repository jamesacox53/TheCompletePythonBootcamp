my_file = open('myFile.txt')

print(my_file.read())

my_file.seek(0)
print(my_file.read())

my_file.seek(0)
contents = my_file.read()
print(contents);

my_file.seek(0)
content_lines = my_file.readlines()
print(content_lines)

my_file.close()

with open('myFile.txt') as my_new_file:
    contents_read = my_new_file.read()
    print('contents read: ' + contents_read)

with open('myFile2.txt', mode='a') as my_new_file2:
    my_new_file2.write('\nthis is the fourth line')

with open('myFile3.txt', mode='w') as my_new_file3:
    my_new_file3.write('I created this file')

with open('myFile3.txt', mode='r') as my_new_file3:
    print(my_new_file3.read())