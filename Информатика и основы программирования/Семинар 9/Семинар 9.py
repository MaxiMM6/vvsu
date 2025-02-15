import pandas as pd
import os
import matplotlib

os.chdir(r'C:\Users\tr0jaNNN\Documents\GitHub\vvsu\Python\Семинар 9')

            #Загрузка и предварительная обработка

#task1-2
df = pd.read_csv('Titanic.csv', index_col = 'PassengerId')

#task3
df = df.dropna()

            #Описание базы данных

#task4
print(df.info())

#task5
print(df.describe())

#task6
ax = df['Age'].plot.hist(color = "red")
ax.set_title('Age')
ax.set_xlabel('Возраст')
ax.set_ylabel('Кол-во людей')

#task7
df['Fare'].describe()

            #Работа со строками и столбцами базы

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
print(df[(df['Class'] == 1) | (df['Class'] == 2)])

#task13
print(df[(df['Survived'] == 1) & ((df['Class'] == 1) | (df['Class'] == 2))])

#task14
df['Female'] = (df['Sex'] == 'female').astype(int)
print(df)

            #Группировка

#task1
print(df.Embarked.unique())

#task2
print(df.groupby('Survived').mean(numeric_only = True))

#task3
age_stats = df.groupby('Sex')['Age'].agg(['mean', 'median'])
print(age_stats)

            #Выгрузка базы в файл

#task1
columns_list = list(df.columns)
lower_list = [x.lower() for x in columns_list]
df.columns = lower_list
print(df.columns)


#task2
new_csv = df.to_csv('Titanic-new.csv')

