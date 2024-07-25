def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

example_row = [1, 2, 3]

display(example_row, example_row, example_row)

print("------------")

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

display(row1, row2, row3)

row2[1] = 'X'

print("------------")

display(row1, row2, row3)