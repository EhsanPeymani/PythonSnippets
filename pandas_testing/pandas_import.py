import pandas as pd

# reading the dataset
data1 = pd.read_csv('cereal.csv')
print(data1.head(1))

# making the column names start with capital
headers = data1.columns
headers = [h.capitalize() for h in headers]

# possible to rewrite the headers
data1.columns = headers

# re-read csv with new header names
data2 = pd.read_csv('cereal.csv', names=headers, header=0)
print(data2.head(1))

# making some of entries for Fat equal to dot '.'
data2.loc[data2['Fat'] == 1, ['Fat']] = '.'
print(data2['Fat'].dtype) # data type changed to object
data2.to_csv('cereal2.csv', index=False)

# dealing with NaN numbers
data3 = pd.read_csv('cereal2.csv', na_values='.')
print(data3.info())