list_of_cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
# for i in list_of_cars:
#     print('Я езжу на автомобиле марки ' + i)
cars_count = 0
for i in range(len(list_of_cars)):
    cars_count += 10
    print('Я езжу на автомобиле марки ' + list_of_cars[i], cars_count)
