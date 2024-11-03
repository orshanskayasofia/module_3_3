def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# print_params(3, 'urban', False, 4.5) - не работает, 4 аргумента вместо 3
print_params(5, 'urban') # - работает, третий аргумент остаётся по умолчанию
print_params(b = 25) # - работает
print_params(c = [1,2,3,]) # - работает

values_list = [3, 'simona', False]
values_dict = {'a': 4, 'b': 'python', 'c': 4.5}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [45.7, 'snow']
print_params(*values_list_2, 78)