my_list=['apple', 'pineapple', 'orange', 'lemon', 'mango', 'peach']
print('List:', my_list)
print('First element:', my_list[0])
print('Last element:', my_list[-1])
print('Sublist:', my_list[2:5]) #исправлено с [2:4] на [2:5]
my_list[2]='melon'
print('Modified list:', my_list)
print('---------------')
my_dict={'apple': 'яблоко', 'pineapple': 'ананас', 'orange': 'апельсин', 'lemon': 'лимон'}
print('Dictionary:', my_dict)
print('Translation:', my_dict.get('orange'))
my_dict['apple']='apple'
print('Modified dictionary:', my_dict)
my_dict.update({'plum': 'слива'})
print('Updated dictionary:', my_dict)
