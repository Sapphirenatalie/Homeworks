immutable_var=(2023, 2024, 'abc', False)
print('Immutable tuple: ', (immutable_var))
# immutable_var[0][0]=2020 #неизменяемый тип
# изменить можно лишь элемент списка, который находится внутри кортежа
# (immutable_var)=([20, 21, 22], 23)
# immutable_var[0][0]=19
# print(immutable_var)
mutable_list=[1, 2, 3, 'letter', True]
print('Mutable list: ', (mutable_list))
mutable_list.append(20)
print(mutable_list)
mutable_list.extend([False])
print(mutable_list)
mutable_list[1]='Fruits'
mutable_list[-1]='Modified'
print(mutable_list)
