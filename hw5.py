immutable_var = ('name', 31, 93, [1, 3])
print(immutable_var)
immutable_var[3][0] = 2     #изменить можно только изменяемые части кортежа
print(immutable_var)

mutable_list = ['name', 's', 93, True, '[1,3]']
print(mutable_list)
mutable_list[3] = 8
print(mutable_list)