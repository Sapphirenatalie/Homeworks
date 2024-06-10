class Building:
    total = 0

    def __init__(self, quantity, floors, types):
        self.numberOfFloors = floors
        self.buildingType = types
        Building.total = quantity

        for i in range(1, Building.total + 1):
            if i <= Building.total:
                print(f'Здание № {i}\n{self.buildingType}\n{self.numberOfFloors} этажей \n')


house = Building(40, 7, 'кирпичный дом')
