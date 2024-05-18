print('Функция с параметрами по умолчанию:')


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

print()
print('Распаковка параметров')

values_list = [7, False, [3, 8]]
values_dict = {'a': 4, 'b': 5, 'c': 6}


def print_params(a, b, c):
    print(a, b, c)


print_params(*values_list)
print_params(**values_dict)

print()
print('Распаковка + отдельные параметры:')

values_list_2 = ['Санкт-Петербург', 1703]


def print_params(a, b, c):
    print(a, b, c)


print_params(42, *values_list_2)
# print_params(*values_list_2, 42) это не работает, так как распаковка должна идти после
