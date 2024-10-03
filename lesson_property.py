# class Box:
#     material = 'peiper'
#
#     def __init__(self, x, y, z):
#         if not isinstance(x, int):
#             raise TypeError('length must be "int"')
#         elif x > 0:
#             self.length = x
#         else:
#             raise ValueError(f'length more then 0, got: {x = }')
#         self.width = y
#         self.height = z
#         self.volume = self.height * self.width * self.height
#
#
# box_1 = Box(1, 2, 3)
# print(box_1.__dict__)
# print(box_1.__class__)
# box_1 = Box(10, 2, 3)
# print(box_1.__dict__)
# print(box_1.__class__)
class Box:
    material = 'peiper'

    def __init__(self, x, y, z):
        # if not isinstance(x, int):
        #     raise TypeError('length must be "int"')
        # elif x > 0:
        #     self.__length = x
        # else:
        #     raise ValueError(f'length more then 0, got: {x = }')
        self.set_length(x)

        if not isinstance(y, int):
            raise TypeError('length must be "int"')
        elif y > 0:
            self.width = y
        else:
            raise ValueError(f'length more then 0, got: {y = }')

        if not isinstance(y, int):
            raise TypeError('length must be "int"')
        elif z > 0:
            self.height = z
        else:
            raise ValueError(f'length more then 0, got: {z = }')

        self.volume = self.__length * self.width * self.height

    def get_length(self):
        return self.__length

    def set_length(self, value):
        if not isinstance(value, int):
            raise TypeError('length must be "int"')
        elif value > 0:
            self.__length = value
        else:
            raise ValueError(f'length more then 0, got: {value = }')


box_1 = Box(1, 2, 3)
# box_1.length = -18
box_1.set_length(10)
print(box_1.get_length())
print(box_1.__dict__)
# print(box_1.__class__)
# box_1 = Box(10, 2, 3)
# print(box_1.__dict__)
# print(box_1.__class__)
