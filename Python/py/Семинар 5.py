#task1

def square(n):
    return n ** 2

n = int(input('Введите число: '))

print(f'Квадрат числа равен: {square(n)}')



#task2

def nums(n):
    return [n - 1, n + 1]

n = int(input('Введите число: '))
result = nums(n)

print(result)
    


#task3

def str_lower(string):
    return [string.lower().split()]

string = input('Введите строку: ')

result = str_lower(string)

print(result)



#task4 

import math

def my_log(num_list):
    log_list = []

    for num in num_list:
        if float(num) > 0:
            log_list.append(math.log(float(num)))
        else:
            log_list.append('None')

    return log_list

num_list = (input('Введите список чисел: ')).split(',')

result = my_log(num_list)
print(result)



#task5

def func():

    names = input('Введите имена людей: ')
    age = input('Введите возраст: ')
    
    names_list = [x for x in names.split()]
    age_list = [x for x in age.split()]

    if len(names_list) == len(age_list):
        dict_name_age = dict(zip(names_list, age_list))

        return dict_name_age
    else:
        print('Списки имеют разную длину.')
        dict_name_age = {}

        return dict_name_age
    
result = func()
print(result)



#task7

def all_sort():

    numbers = input('Введите перечень чисел: ')
    numbers_list = [int(x) for x in numbers.split(',')]

    return sorted(numbers_list)

result = all_sort()
print(result)
