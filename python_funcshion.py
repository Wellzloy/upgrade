a = [1, 4, [2, [3, [4, [5, [6, [7, [8, [9, [[[55]]]]]],45]]]]]]
list_string_numbers = str(a).replace('[','').replace(']','').split(', ')
sum_number = 0
i = 0
while i < len(list_string_numbers):
    sum_number = sum_number + float(list_string_numbers[i])
    i = i + 1
print(sum_number)




