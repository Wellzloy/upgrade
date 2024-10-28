def add_everything_up(a, b):
    try:
        number = f'{(a + b):.3f}'
        return number

    except TypeError:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
