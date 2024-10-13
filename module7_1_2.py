class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'<{self.name}, {self.weight}, {self.category}>'


class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        content = file.read()
        file.close()
        return content

    def add(self, *products):
        existing_names = set()
        new_products = []
        errors = []

        file = open(self.__file_name, 'r')
        lines = file.readlines()
        file.close()

        for line in lines:
            parts = line.strip().split(', ')
            existing_names.add(parts[0])

        for product in products:
            if product.name not in existing_names:
                new_products.append(product)
            else:
                (errors.append(f'Продукт "{product.name}" уже есть в магазине'))

            print(product.name, 'имена продуктоа')




        if len(new_products) > 0:
            file = open(self.__file_name, 'a')
            for product in new_products:
                file.write(f'{product}\n')
            file.close()


        return new_products, errors




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
#Этот код описывает метод add класса Shop. Он принимает список продуктов (*products) и выполняет следующие действия:

#     Создает три переменные:
#         existing_names: множество существующих имен продуктов.
#         new_products: список новых продуктов, которые еще не существуют в магазине.
#         errors: список ошибок, возникающих при попытке добавить уже существующий продукт.
#     Открывает файл с именем __file_name для чтения (r).
#     Считывает все строки из файла и сохраняет их в переменную lines.
#     Закрывает файл.
#     Проходит по каждой строке в lines.
#     Разбивает каждую строку на части с помощью split, удаляет пробелы с конца строк с помощью strip и добавляет
#     первую часть (имя продукта) в множество existing_names.
#     Проходит по каждому продукту в списке products.
#     Если имя продукта (product.name) не находится в множестве existing_names, добавляет его в список new_products.
#     Если имя продукта уже существует в множестве existing_names, добавляет сообщение об ошибке в список errors.
#
# Когда метод завершается, он возвращает список новых продуктов и список ошибок.