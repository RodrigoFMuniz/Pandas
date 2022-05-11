import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
df2 = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)
print('-------------------')
print(df.loc[0])
print('-------------------')
print(df.loc[[0, 1]])
print('-------------------')
print(df2)
print('-------------------')
print(df2.loc["day2"])
