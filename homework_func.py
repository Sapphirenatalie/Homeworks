def print_params(day_of_week):
    print('Today is:', day_of_week)


print_params('Monday')
print_params('Tuesday')
print_params('Wednesday')
print_params('Thursday')
print_params('Friday')
print_params('Saturday')
print_params('Sunday')

print('---------------------')
#последовательный вывод дней недели функция плюс цикл for:
def print_params(day_of_week):
    day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in day_of_week:
        print('Today is ' + i)


print_params(day_of_week='i')
