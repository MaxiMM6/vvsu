# Семинар 1



#task 0

a = [1, 0, 9, 12, 18, 34, 89, 91, 33, 127]
b = [2, 8, 9, 11, 76, 25, 44]

print(a[0], a[2], a[-1])

b.append(7)

b[4] = 8

merged = a + b
print(merged)

c = a[:-1]
c.append(100)
print(c)




#task1

girls = ["Иветта", "Виолетта", "Кассандра", "Вирджиния", "Амелия", "Розамунда", "Янина"]
girls.append("Беатриса")
print(girls[1:5])
print(girls[3:])
print(girls[:5])
print([girls[2]], [girls[4:6]])




#task2

l = [12, 3, 8, 125, 10, 98, 54, 199]

import math
print(l)
print([math.log10(x) for x in l])

l[4] = 0
print(l)
print([math.log(x) for x in l])


#task3

age = [24, 35, 42, 27, 45, 48, 33]

age2 = [i**2 for i in age]
print(age2)



#task4

numbers = [1, 5, 6, 8, 10, 21, 25, 1, 0, -9, 9]

num = int(input("Введите целое число от 1 до 10: "))

result = numbers[num - 1]
print(result)


#task5

l = [1,2,3,4]
for i in range(len(l)):
    a = l[i] + l[i-1]
    print(a)