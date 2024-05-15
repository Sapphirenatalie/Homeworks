# вывод всех паролей к числам от 3 до 20:
for k in range(3, 21):
    str_ = ""
    for i in range(1, 21):
        for j in range(1, 21):
            sum_ = (i + j)
            if sum_ % k == 0 and sum_ == k and i < j:
                str_ += str(i) + str(j)
    print(k, '-', str_)

print('----------------------')
# вывод пароля в зависимости от введенного числа:
while True:
    number_ = int(input("Введите число от 3 до 20: "))
    if 2 < number_ < 21:
        str_ = ""
        for i in range(1, 21):
            for j in range(1, 21):
                sum_ = (i + j)
                if sum_ % number_ == 0 and sum_ == number_ and i < j:
                    str_ += str(i) + str(j)
    print('Пароль: ', str_)
    break
