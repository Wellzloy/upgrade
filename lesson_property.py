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
        if not isinstance(x, int):
            raise TypeError('length must be "int"')
        elif x > 0:
            self.length = x
        else:
            raise ValueError(f'length more then 0, got: {x = }')
        self.width = y
        self.height = z
        self.volume = self.height * self.width * self.height

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


        self.volume = self.height * self.width * self.height


    def


box_1 = Box(1, 2, 3)
box_1.length = -18
print(box_1.length)
print(box_1.__dict__)
print(box_1.__class__)
box_1 = Box(10, 2, 3)
print(box_1.__dict__)
print(box_1.__class__)