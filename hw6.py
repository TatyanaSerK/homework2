my_list = ['apple', 'banana', 'peach', 'mango', 'lemon', 'pear']
print('список: ', my_list)
print('первый элемент: ', my_list[0])
print('последний элемент: ', my_list[-1])
print('подСписок с 3 по 5: ', my_list[2:5])
my_list[2] = "pineapple"
print('новый список: ', my_list)

my_dict = {'apple': 'яблоко', 'banana': 'банан', 'mango': 'манго', 'lemon':'апельсин?'}
print('словарь: ', my_dict)
print('перевод для "lemon"', my_dict['lemon'])
my_dict['lemon'] = 'лимон'
print('исправленный словарь', my_dict)
my_dict['orange'] = 'апельсин'
print('добавлен перевод "orange"', my_dict)