x = 38
print('Здравствуйте!')
if x < 0:
    print('меньше нуля')
print('До свидания!')

x = -1
print('Здравствуйте!')
if x < 0:
    print('меньше нуля')
print('До свидания!')

#примеры

a, b = 10, 5
if a > b:
    print('a > b')
if a > b and a > 0:
    print('успех_1')
if (a > b) and (a > 0 or b < 1000):
    print('успех_2')
if 5 < b and b < 10:
    print('успех_3')

#можно сравнивать числа, строки, списки...
if '34' > '123':
    print('успех 1')
if '123' > '34':
    print('успех 2')
if [1, 2] > [1, 1]:
    print('успех 3')

# нельзя сравнивать разные типы
#if '6' > 5:
#    print('успех')
#if [5, 6] > 5:
#    print('успех')
#но
if '6' != 5:
    print('успех')