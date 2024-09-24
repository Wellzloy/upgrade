class House:
    def __init__(self, name, number_of_floors):
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
        return (self.number_of_floors == other.number_of_floors)
    def __lt__(self, other):
        return (self.number_of_floors < other.number_of_floors)
    def __le__(self, other):
        return (self.number_of_floors <= other.number_of_floors)
    def __gt__(self, other):
        return (self.number_of_floors > other.number_of_floors)
    def __ge__(self, other):
        return (self.number_of_floors >= other.number_of_floors)
    def __le__(self, other):
        return (self.number_of_floors != other.number_of_floors)




# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=)
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

print(h1 == h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)


# a = 5.5
# print(isinstance(House, (str)))