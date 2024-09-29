class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        new_object = super().__new__(cls)
        cls.houses_history.append(args[0])
        return new_object

    def __init__(self, name, number_of_floors):
        self.new_floor = None
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor > self.number_of_floors or 1 > self.new_floor:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors} '

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            raise TypeError('other does not belong to the House class')

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            TypeError('value does not belong to the int class')

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        self.number_of_floors = value + self.number_of_floors
        return self

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)

del h2
del h3

print(House.houses_history)
