my_dict = {'Alex': 1987, 'Oleg': 1958, 'Jan': 2020, 'Valera': 1992}
print('Словарь: ', my_dict)
print('Год рождения Алекса: ', my_dict.get('Alex'))
print('Несуществующее значение: ', my_dict.get('Kris'))
my_dict.update({'Max': 1452, 'Dmitrii': 1605})

a=my_dict.pop('Valera')
print('Удаленное значение: ',a)
print('Дополненный словарь: ',my_dict)
my_set = {1, 2, 3, True, "string", 3.14}
print('Множество: ', my_set)
my_set.add(7)
my_set.add(4.2565)
my_set.discard(3)
print('Обновленное множество: ',my_set)
