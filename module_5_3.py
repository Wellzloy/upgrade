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

    def __add__(self, value):
        return self.number_of_floors + value

    def __radd__(self, value):
        return self.__add__(value)







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






h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__


print(h1)
h1 = h1 + 10 # __add__
print(h1)


#print(h1 == h2)

#h1 += 10 # __iadd__
#print(h1)

# h2 = 10 + h2 # __radd__
# print(h2)

# print( h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__


class Count(object):
    def __init__(self, count):
        self._count = count

    def __add__(self, other):
        total_count = self._count + other._count
        return Count(total_count)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __str__(self):
        return 'Count:% i' % self._count


c2 = Count(2)
c3 = 0 + c2
print(c3)
