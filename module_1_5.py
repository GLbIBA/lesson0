immutable_var = 1,2,True,'python'
print(immutable_var)
#immutable_var[0] = 3 TypeError: кортеж не поддерживает обращение поэлементно

mutable_list = [10, 58,True, 15, 2, 'python']
mutable_list[0], mutable_list[2], mutable_list[4] = 265, 13, 'banana'
print(mutable_list)
