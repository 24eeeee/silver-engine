import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.options.display.expand_frame_repr = False

df = pd.read_csv('data/titanic.csv')

print(df.head(10))

plt.title("Количество выживших:")
df['Survived'].value_counts().plot(kind='pie', autopct='%1.0f%%')
plt.show()

plt.title("Выжившие в зависимости от класса и пола")
df.groupby(["Pclass", "Sex"])["Survived"].value_counts(normalize=True).sort_values().plot(kind='bar')
plt.show()


sum18_1 = df[df['Age'] < 18][df['Survived'] == 1].groupby(["Age"])["Survived"].value_counts().sum()
sum55_1 = df[df['Age'] < 55][df['Age'] >= 18][df['Survived'] == 1].groupby(["Age"])["Survived"].value_counts().sum()
sum100_1 = df[df['Age'] >= 55][df['Survived'] == 1].groupby(["Age"])["Survived"].value_counts().sum()
sum18_0 = df[df['Age'] < 18][df['Survived'] == 0].groupby(["Age"])["Survived"].value_counts().sum()
sum55_0 = df[df['Age'] < 55][df['Age'] >= 18][df['Survived'] == 0].groupby(["Age"])["Survived"].value_counts().sum()
sum100_0 = df[df['Age'] >= 55][df['Survived'] == 0].groupby(["Age"])["Survived"].value_counts().sum()
pd.DataFrame([sum18_1/891, sum55_1/891, sum100_1/891 ,sum18_0/891, sum55_0/891, sum100_0/891],
             columns=['Количество выживших'],
             index=['Выжившие < 18', 'Выжившие < 55', 'Выжившие >= 55', 'Погибшие < 18', 'Погибшие < 55', 'Погибшие >= 55' ])\
    .sort_values('Количество выживших').plot(kind='bar', title='Выжившие в зависимости от возраста')
plt.show()
