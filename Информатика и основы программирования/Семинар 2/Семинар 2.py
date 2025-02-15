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

dohod = input("Введите доходы через пробел: ").split()

l = [int(i) for i in dohod]

l_log = [math.log10(x) for x in l]

print(l_log)



#task5

words = ["Speak ","to", "me ", "of", "Florence", "And ", "of", "the", "Renaissance"]

words_clean = [i.strip().lower() for i in words]

print(words_clean)
