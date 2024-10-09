# Семинар 1 (дополнение)



#task1

day = int(input("Укажите день: "))
minutes = (day - 1) * 3 + 1

print(f"В день #{day}: {minutes} минут/ы.")




#task2

user_name = input("Введите: Имя, Фамилию: ")
print(f"{user_name}, добро пожаловать!")




#task3

course_1 = input("Введите название 1 курса: ")
course_2 = input("Введите название 2 курса: ")
course_3 = input("Введите название 3 курса: ")

print('Рецепт')
print(f'{course_1}: 200 г')
print(f'{course_2}: 300 г')
print(f'{course_3}: 100 г')
print('Приправить политической историей. Добавить математические модели по вкусу.')




#task4

course1 = float(input("Введите массу политической теории в граммах: "))
course2 = float(input("Введите массу истории политических учений в граммах: "))
course3 = float(input("Введите массу математики в граммах: "))

course1_kg = float(course1 / 1000)
course2_kg = float(course2 / 1000)
course3_kg = float(course3 / 1000)

print('Рецепт')

print('Политическая теория: %.3f кг' % (course1_kg))
print('история политических учений: %.3f кг' % course2_kg)
print('Математика: %.3f кг' % (course3_kg))

print('Приправить политической историей. Добавить математические модели по вкусу.')