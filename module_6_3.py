class Vehicle:
    vehicle_type = None    
    # задании указано "none" (строка с текстом "none").
    # Замена на спец. тип данных None в данном задании ничего не изменяет.
    # Поэтому я поставила None из-за красоты восприятия.
    
    def __init__(self, vehicle_type):
        Vehicle.vehicle_type = vehicle_type


class Car:
    price = 1000000

    def __init__(self, price):
        Car.price = price

    def horse_powers(self):
        horse_power = 90
        return f'Мощность: {horse_power} л.с.'


class Nissan(Vehicle, Car):
    def __init__(self, vehicle_type, price):
        super().__init__(price)
        super().__init__(vehicle_type)
        super().horse_powers()

        print(f'Автомобиль {__class__.__name__} {vehicle_type}, Цена: {price}, {super().horse_powers()}')

    def horse_powers(self):
        horse_power = 102
        return f'Мощность: {horse_power} л.с.'


if __name__ == '__main__':
    car = Nissan('Almera', 1000000)
    print(car.vehicle_type)
    print(car.price)

    print('\nПереопределение свойств price и vehicle_type, и функции horse_powers')
    car.vehicle_type = 'X-Trail'
    car.price = 2500000
    car.horse_powers()

    print(f'Автомобиль {Nissan.__name__} {car.vehicle_type}, Цена: {car.price}, {car.horse_powers()}')

    print(car.vehicle_type)
    print(car.price)
