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
w = (str(data_structure).replace('[', '').replace(']', '')
     .replace('{', '').replace('}', '')
     .replace('(', '').replace(')', '')).split(', ')
print(type(data_structure))
print(w)
# print(w[3])
# print(len(w[3]))
# print(w[4])
# print(len(w[4]))
for i in w:
    print(i)

