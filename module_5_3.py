

class Building:

    def __init__(self, floors, types):
        self.numberOfFloors = floors
        self.buildingType = types
        print('кол-во этажей -', self.numberOfFloors, ', тип объекта - ', self.buildingType)

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


house_1 = Building(10, 'панельный дом')
house_2 = Building(5, 'кирпичный дом')
print()

print(house_1 == house_2)
if house_1 == house_2:
    print('дома одинаковые')
else:
    print('дома различаются')
print()
house_2.buildingType = 'панельный дом'
house_2.numberOfFloors = 10
print(house_1 == house_2)
if house_1 == house_2:
    print('дома одинаковые')
else:
    print('дома различаются')

