import pandas as pd
import os
import matplotlib

os.chdir(r'C:\Users\zhlya\Documents\GitHub/vvsu/Python/py/Семинар 9')

#task1-2
df = pd.read_csv('Titanic.csv', index_col = 'PassengerId')

#task3
df = df.dropna()

#task4
print(df.info())

#task5
print(df.describe())

#task6
print(df['Age'].plot.hist(color = "red"))

#task7
df['Fare'].describe()

#task8
columns_list = list(df.columns)
print(columns_list)

#task9
columns_list[1] = 'Class'
df.columns = columns_list
print(df.columns)

#task10
print(df[df['Sex'] == 'female'])

#task11
Ymale = df[(df['Survived'] == 1) & (df['Sex'] == 'male') & (df['Age'] < 32)]

#task12
class_1_2 = df[(df['Class'] == 1) | (df['Class'] == 2)]

#task13
class_1_2_surv = df[(df['Survived'] == 1) & ((df['Class'] == 1) | (df['Class'] == 2))]

#task14