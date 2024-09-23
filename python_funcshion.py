# a = [1, 4, [2, [3, [4, [5, [6, [7, [8, [9, [[[55]]]]]], 45]]]]]]
# list_string_numbers = str(a).replace('[', '').replace(']', '').split(', ')
# sum_number = 0
# i = 0
# while i < len(list_string_numbers):
#     sum_number = sum_number + float(list_string_numbers[i])
#     i = i + 1
# print(sum_number)

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
list_values = (str(data_structure).replace('[', '').replace(']', '')
     .replace('{', '').replace('}', '')
     .replace('(', '').replace(')', '')
     .replace(':', ',').replace("'", "")).split(', ')
print(type(data_structure))
print(list_values)
sum_value = 0
i = 0
while i < len(list_values):
    value = list_values[i]
    if value.isdigit():
        sum_value = sum_value + float(value)
        print(value, sum_value)
    else:
        sum_value = sum_value + len(value)
    i = i + 1




