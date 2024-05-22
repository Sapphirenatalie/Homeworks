def test(codes, *types, region='Санкт-Петербург', **values): # Функция с произвольным числом параметров разного типа
    for key, value in values.items():
        print(key, value)
    print(types)


test('автомобильные номера', 98, 178, 198, region='Санкт-Петербург', code='98',
     region_code='Санкт-Петербург - 98')

print('-----------')

def factorial(n): # Рекурсивная функция - факториал числа n
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

print('-----------')

n = int(input("Введите число: ")) # Рекурсивная функция - факториал числа n + input


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(n))