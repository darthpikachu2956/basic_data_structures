my_dict = {'Charlie': 2008, 'Nick': 2006, 'Harry': 2007}
print('Dictionary:', my_dict)
print('Existing value:', my_dict['Charlie'])
print('Not existing value:', my_dict.get('Christian'))
my_dict.update({'Sarah': 1979, 'Tara': 2006})
a = my_dict.pop('Harry')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

my_set = {2, 3, 'Party', 'Party', True, True, 2, 6}
print('Set:', my_set)
my_set.add('Paris')
my_set.add(5.2)
my_set.remove(2)
print('New set:', my_set)
