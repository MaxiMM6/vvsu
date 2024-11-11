#task1

#A
def multi(num):
    return num * var + 7

var = 11
numbers = [12, 24, 36, 48, 109, 187]
new_numbers = list(map(multi, numbers))

print(new_numbers)

#B

numbers = [12, 24, 36, 48, 109, 187]
result = list(map(lambda x: x * 7, numbers))
print(result)



#task2

my_number = [7, 9, 6, 1, 9, 6, 8, 4, 7, 1, 7]
another_number = [7, 9, 2, 4, 7, 8, 3, 9, 3, 2, 3]

new_number = list(map(lambda x, y: x * y, my_number, another_number))

print(new_number)



#task3

my_number = [7, 9, 6, 1, 9, 6, 8, 4, 7, 1, 7]
var = 11

new_number = list(map(lambda x: x * var, my_number))

odd = list(filter(lambda y: y % 2 == 0, new_number))
even = list(filter(lambda z: z % 2 != 0, new_number))

odd = list(map(lambda y: True, odd))
even = list(map(lambda z: False, even))

print(new_number)
print(odd)
print(even)



#task4

my_number = ['7', '9', '6', '1', '9', '6', '8', '4', '7', '1', '7']
var = '4'

#A
int_division = list(map(lambda x: int(x) // int(var), my_number))
print(f'#A {int_division}')

#B
float_division = list(map(lambda x: int(x) / int(var), my_number))
print(f'#B {float_division}')





