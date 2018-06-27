import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cereal.csv', index_col='name')

features = ['calories', 'protein', 'fat', 'sodium', 'sugars']
df = df[features]
print(df.head(2))

# closing all figues
plt.close('all')

# creating a numpy array from 'calories' and plot
calories = df['calories'].values
print('Type of calories is {}'.format(type(calories)))
plt.plot(calories)
plt.ylabel('calories')
plt.show()

# plotting pandas Series - show index on the x-axis
calories_series = df['calories']
print('Type of calories_series is {}'.format(type(calories_series)))
plt.plot(calories_series.iloc[:10])
plt.ylabel('calories')
plt.xticks(rotation=90)
plt.show()

# plotting using pandas.DataFrame.plot
# plotting all Series on one plot
df.plot()
plt.show()

# similar to df.plot(), you can use plt.plot(df) to plot all series in one plot
# it does not show legend !!!
plt.plot(df)
plt.show()

# changing to logarithmic scale
df.plot()
plt.yscale('log') # logarithmic scale on the y scale
plt.show()

# customizing example
df['sodium'].iloc[0:10].plot(color='b', style='-*', legend=True)
df['sugars'].iloc[0:10].plot(color='r', style='.-', legend=True)
plt.xlabel('')
plt.xticks(rotation=90)

# saving figs
plt.savefig('test.pdf')
plt.savefig('test.png')
# plt.savefig('test.jpg')

plt.show()
