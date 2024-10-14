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

        current_products = self.get_products().split('\n')

        for product in current_products:
            if product != '':
                parts = product.strip().split(', ')
                existing_names.add(parts[0].replace('<', ''))

        for product in products:
            if product.name not in existing_names:
                new_products.append(product)
            else:
                errors.append(print(f'Продукт {product.name} {product.weight} {product.category} уже есть в магазине'))

        if len(new_products) > 0:
            file = open(self.__file_name, 'a')
            for product in new_products:
                file.write(f'{product}\n')
            file.close()

        return new_products, errors


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())