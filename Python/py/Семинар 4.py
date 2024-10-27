'''#task1

rept = {"python" : " питон",
        "anaconda" : "анаконда",
        "tortoize" : " черепаха" }

rept["snake"] = "змея"
rept["tortoise"] = rept["tortoize"]
rept.pop('tortoize')

for k, v in rept.items():
    print(f'{k.capitalize()} по-английски будет {v}.')



#task2 

cnt = ["Andorra", "Belarus", "Denmark",
       "Kenya", "Jamaica", "Romania"]
fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]

dict = {}

for i in range(len(cnt)):
    dict[cnt[i]] = fh[i]
    
print(dict)



#task3

pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]

calc = {}

for i in pairs:
    calc[i] = i[0] * i[1]

print(calc)'''



#task4

grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5,
          'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
          'Ursula': 4, 'Viktor': 5}

excel = []
good = []
satisf = []
bad = []

for k, v in grades.items():
    if v == 2:
        bad.append(k)
    elif v == 3:
        satisf.append(k)
    elif v == 4:
        good.append(k)
    else:
        excel.append(k)

print(f'Excel = {excel}')
print(f'Good = {good}')
print(f'Satisf = {satisf}')
print(f'Bad = {bad}')
