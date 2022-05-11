import pandas as pd
names = ['Rodrigo', 'Fernando', 'Jéssica']
data = pd.Series(names)
data_index = pd.Series(names, ['nome 1', 'nome 2', 'nome 3'])
print(data)
print(data_index)
print(data_index['nome 1'])