color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
multiply = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

first = input()
second = input()
third = input()

first_value = value[color.index(first)]
second_value = value[color.index(second)]

print(int(str(first_value)+str(second_value))*multiply[color.index(third)])