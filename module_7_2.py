def custom_write(file_name, strings):
    file = open(file_name, 'r')
    print(file.name)
    print(file.read())
    file.close()
    print(strings)
    file = open(file_name, 'w')
    for string in strings:
        file.write(string + '\n', encoding='utf-8')
    file.close()





info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
# for elem in result.items():
#   print(elem)

