#task1

def square(x):
    result = x ** 2
    return result
  
    print(f"Квадрат числа равен: {result}")
     
    print(f"Квадрат числа равен: {result}")
    return result
print(square(5))



#task2

def nums(n):
    return [n - 1, n + 1]

print(nums(7))



#task3

def str_lower(string):
    return [string.lower().split()]

print(str_lower('В лесу родилась ёлочка В лесу она росла'))



#task4

import math

def my_log(l):
    
    log_list = []

    for num in l:
        if float(num) > 0:
            log_list.append(math.log(num))
        else:
            log_list.append('None')
        
    return log_list


print(my_log([1, 3, 2.5, -1, 9, 0, 2.71]))



#task5 

def func(list1, list2):

    new_dict = {}

    if len(list1) == len(list2):
        new_dict = dict(zip(list1, list2))
    else:
        print('Списки имеют разную длину')
    
    return new_dict

print(func(['Ann', 'Tim', 'Sam'], [12, 23, 17]))
print(func(['Ann', 'Tim', 'Sam'], [12, 23, 17, 19]))



#task6

def factorial_(n):
    f = 1

    for i in range(2, n + 1):
        f *= i
    return f

print(factorial_(5))

def binom_prob(k, n):

    C = factorial_(n) // factorial_(k) * factorial_(n - k)
    return C

print(binom_prob(2, 3))



#task7

def all_sort(*args):

    num = [int(numbers) for numbers in args]
    
    for i in range(len(num)):
        for x in range(0, len(num) - i - 1):
            if num[x] > num[x + 1]:
                num[x], num[x + 1] = num[x + 1], num[x]
    return num

print(all_sort(7,6,1,3,8,0,-2))

