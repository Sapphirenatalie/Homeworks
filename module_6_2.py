class Vehicle:  # любой транспорт
    __COLOR_VARIANTS = ['dark_blue', 'red', 'metallic', 'green', 'black', 'white']

    def __init__(self, owner: str, __model: str, __engine_power: str, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        print(f'Модель: {self.__model}\nМощность двигателя: {self.__engine_power}\nЦвет: {self.__color}\n'
              f'Владелец: {self.owner}\n')

    def set_color(self, new_color: str):
        self.__color = new_color

        if self.__color.isupper():
            return new_color.islower()
        if new_color in self.__COLOR_VARIANTS:
            return new_color
        else:
            print('Нельзя сменить цвет на ', new_color)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle2 = Sedan('Vasyok', 'Toyota Mark II', 500, 'black')


print('Изначальные свойства vehicle1\n')
vehicle1.print_info()

print('Меняем свойства (в т.ч. вызывая методы)')
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

print('\nПроверяем что поменялось')
vehicle1.print_info()

print('Изначальные свойства vehicle2\n')
vehicle2.print_info()

print('Меняем свойства (в т.ч. вызывая методы)')
vehicle2.set_color('AQUA')
vehicle2.set_color('RED')
vehicle2.owner = 'Alex'

print('\nПроверяем что поменялось')
vehicle2.print_info()
