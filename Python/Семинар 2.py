'''#task1

fio = input("Введите Ваши ФИО: ")

surname, name, patronymic = fio.split()


print(f"Ваша фамилия: {surname}")
print(f"Ваше имя: {name}")
print(f"Ваше отчество: {patronymic}")'''



'''#task2

a = "1; 2; 3; 100"

b = list(a)
print(b)'''



'''#task3

a = input("Введите номер телефона через дефис: ")

b = a.replace("-", "")

print(b)'''



'''#task4 

import math

l = []

l2 = [log10(x) for x in l]
print(l2)'''



#task5

words = ["Speak ","to", "me ", "of", "Florence", "And ", "of", "the", "Renaissance"]

words_clean = words.lower()
print(words_clean)