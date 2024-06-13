immutable_var = (2, 3, 'Manchester', True)
# print(immutable_var)
# immutable_var[1] = 300 /// Тип данных "кортеж" является неизменяемым, поэтому его элементы поменять нельзя.
print('Immutable: ', immutable_var)
mutable_list = ['Sidious', 'Maul', 'Tyranus']
print('Mutable: ', mutable_list)
mutable_list.append('Vader')
print('Mutable: ', mutable_list)
mutable_list[0] = 'Plagueis'
print('Mutable: ', mutable_list)
