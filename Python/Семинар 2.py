#task1

fio = input("Введите Ваши ФИО: ")

surname, name, patronymic = fio.split()

print(f"Ваша фамилия: {surname}")
print(f"Ваше имя: {name}")
print(f"Ваше отчество: {patronymic}")



#task2

a = "1; 2; 3; 100"

a_list = a.split("; ")
a_int = []
a_list = [a_int.append(int(n)) for n in a_list]

print(a_int)


a_float = [float(i) for i in a_int]

print(a_float)


#task3

a = input("Введите номер телефона через дефис: ")

b = a.replace("-", "")

print(b)



#task4 

import math

l = [12304, 123024, 54604, 2340]

l2 = [math.log10(x) for x in l]

print(l2)



#task5

words = ["Speak ","to", "me ", "of", "Florence", "And ", "of", "the", "Renaissance"]

words_clean = [i.strip().lower() for i in words]

print(words_clean)
