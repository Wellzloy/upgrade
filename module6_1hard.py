class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), filled=True):
        self.__sides = []
        self.__color = color
        self.filled = filled
    def get_color(self):
        return self.__color

    # Пример использования


figure = Figure((255, 0, 0))  # Красный цвет
print(figure.get_color())  # Выводит (255, 0, 0)