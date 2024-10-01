# from pprint import pprint
# def fill_list(width, element):
#     result = []
#     i = 0
#     while i < width:
#         result.append(element+i)
#         i +=1
#     return result
#
# def get_matrix(x, y, value):
#     result = []
#     i = 0
#     while i < y:
#         result.append(fill_list(x, value))
#         i += 1
#     return result
#
#
#
#
#
#
#
# #print(get_matrix(2, 2, 8))
# pprint(get_matrix(5, 3, 8), width=25)

# data = (4.5, 8.7, True, 8 )
# s = 0
# for x in data:
#     if isinstance(x, int):
#         s += x
#
# print(s)

# class CustomNumber:
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         if isinstance(other, CustomNumber):
#             return CustomNumber(self.value + other.value)
#         else:
#             return CustomNumber(self.value + other)
#     def __radd__(self, other):
#         return self.__add__(other)
#
#
# a = CustomNumber(5)
# b = CustomNumber(10)
# print((a + b).value)  # Вывод: 15
# print((a + 2).value)  # Вывод: 7
# print((3 + a).value)  # Вывод: 8
# class Box:
# box_length = 10
# box_width = 5
# box_height = 11

# box_1 = Box()
#
# print(box_1, box_1.box_length, box_1.box_width, box_1.box_height)
# print(box_1.__dict__)

# box_2 = Box()
# print(box_2, box_2.box_length, box_2.box_width, box_2.box_height)
#
# box_3 = Box()
# print(box_3, box_3.box_length, box_3.box_width, box_3.box_height)

class Box:
    material = 'peiper'
    def __init__(self, x= 5, y = 3, z = 8):
        self.box_length = x
        self.box_width = y
        self.box_height = z


    def get_volume(self):
        volume = self.box_length*self.box_width*self.box_height
        return volume


box_1 = Box(1, 2, 3)
box_1.material = 'glass'
Box.material = 'ais'
print(box_1.get_volume())
print(box_1.__dict__)
box_1.box_length = 15
print(box_1.get_volume())
print(box_1.__dict__)
box_2 = Box()
print(box_2.get_volume())
print(box_2.__dict__)
print(box_2.material)

