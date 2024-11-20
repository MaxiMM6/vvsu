import pandas as pd
import os
import matplotlib

os.chdir(r'C:\Users\zhlya\Documents\GitHub/vvsu/Python/py/')

#task1-2
df = pd.read_csv('Titanic.csv', index_col = 0)

#task3
df = df.dropna()

#task4
print(df.info())

#task5
print(df.describe())

#task6
print(df['Age'].plot.hist(color = "red"))

#task7


#task8
columns_list = list(df.columns)
print(columns_list)

#task9
columns_list[1] = 'Class'
df.columns = columns_list
print(df.columns)

#task10
print(df[df['Sex'] == 0])
