import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles
import pandas as pd

#Завдання 1

data = {
    'Name': ['Alex', 'Bella', 'Chris'],
    'Age': [30, 25, 35],
    'City': ['Kyiv', 'Lviv', 'Odesa']
}
df = pd.DataFrame(data)

df['Salary'] = [50000, 60000, 55000]
df = df.drop(columns=['Age'])
new_row = pd.DataFrame([{
    'Name': 'Diana',
    'City': 'Dnipro',
    'Salary': 58000
}])

df = pd.concat([df, new_row], ignore_index=True)
df = df.drop(index=0)
df['Department'] = 'Sales'
df = df.drop(columns=['Salary'])

print(df)

#Завдання 2

data = {
    'Product': ['Book', 'Pen', 'Notebook'],
    'Price': [15, 2, 5],
    'Stock': [100, 500, 200]
}
df = pd.DataFrame(data)

df['Discount'] = '10%'
df = df.drop(columns=['Stock'])
new_row = pd.DataFrame([{
    'Product': 'Pencil',
    'Price': 1,
    'Discount': '5%'
}])

df = pd.concat([df, new_row], ignore_index=True)
df = df.drop(index=1)
df['Supplier'] = 'Stationery Co.'
df = df.drop(index=2)

print(df)

# #Завдання 3
# #Завдання 4