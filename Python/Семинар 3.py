#task1


user_input = float(input())

if user_input > 0:
    print("Молодец!")
else:
    print("Это не положительное число.")



#task2

marks = input("Введите оценки от 1 до 10 через пробел: ").split()

marks = [int(x) for x in marks]

for i in marks:
    if 1 <= i <= 10:
        print(i)
        if i <= 3:
            print("Плохо")
        elif 4 <= i <= 6:
            print("Удовлетворительно")
        elif 7 <= i <= 9:
            print("Хорошо")
        else:
            print("Отлично")



#task3

user_password = input("Введите пароль: ")

correct_password = '12345'

if user_password == correct_password:
    print('Login success')
else:
    print('Incorrect password, try again!')


#task4

favorites = [3, 7, 11, 23, 18, 48, 81]

integer_number = int(input("Введите целое число: "))

if integer_number not in favorites:
    print('Эх, ну почему?')

else:
    print("Мое любимое число!")



#task5

user_number = int(input("Введите число: "))

if user_number % 2 == 0:
    print('Это число четное')

else:
    print("Это число нечетное")

    

#task6

user_noun = input('Введите существительное: ')

if user_noun.istitle():
    print('Это имя собственное')

else:
    print('Это имя нарицательное')