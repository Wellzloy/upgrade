# def personal_sum(numbers):
#     result = 0
#     incorrect_data = 0
#
#     for item in numbers:
#         try:
#             result += float(item)  # Попытка привести элемент к числу
#         except TypeError:
#             incorrect_data += 1  # Увеличение счетчика некорректных данных
#
#     return result, incorrect_data
#
#
# def calculate_average(numbers):
#     try:
#         sum_result, incorrect_data = personal_sum(numbers)
#
#         if len(numbers) == 0 or incorrect_data == len(numbers):
#             return 0  # Возвращает 0, если коллекция пустая или все элементы некорректны
#
#         average = sum_result / len(numbers)
#         return average
#
#     except TypeError:
#         print("В numbers записан некорректный тип данных")
#         return None
#
def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
    # print(f'Обработано {incorrect_data} неверных данных.')
    return result, incorrect_data


if __name__ == "__main__":
    mix_list = [1, 2, 'a',4, 5, None, 6]
    total_sum, incorrect_count = personal_sum(mix_list)
    print(f'Сумма чисел: {total_sum}, Колличество некорректных данных: {incorrect_count}')

#    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
#    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
#     print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
#     print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать