from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=True):
        self.__color = color
        self.__sides = [*sides]
        self.filled = filled

    def get_color(self):
        if self.filled is True:
            return self.__color
        if self.filled is False:
            return [*self.__color]

    @staticmethod
    def __is_valid_color(*rgb):
        for item in rgb:
            if 0 <= item <= 255 and isinstance(item, int):
                return True
            else:
                return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]
            self.filled = True
        else:
            self.filled = False

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        if self.sides_count != len(sides):
            sides = []
        for i in sides:
            if isinstance(i, int) and self.sides_count == len(sides):
                return True
        else:
            return False

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = [*sides]

    def __len__(self):
        return sum(self.get_sides())


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sum(self.get_sides()) / 2 * pi

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = (2 * self.get_square()) / (self.get_sides()[0])

    def get_square(self):
        return sqrt((sum(self.get_sides()) / 2) *
                    ((sum(self.get_sides()) / 2) - self.get_sides()[0]) *
                    ((sum(self.get_sides()) / 2) - self.get_sides()[1]) *
                    ((sum(self.get_sides()) / 2) - self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides * self.sides_count)

    def get_volume(self):
        return self.get_sides()[0] ** 3


# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


# Выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216
