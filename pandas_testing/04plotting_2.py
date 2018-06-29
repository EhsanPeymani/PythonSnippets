import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cereal.csv', index_col='name')

features = ['calories', 'protein', 'fat', 'sodium', 'sugars']
df = df[features]

print(df.head(2))

# close all figs
plt.close('all')


# line plot
df.plot(x='sugars', y='calories')
plt.title('calories vs. sugar - line plot a bad choice')
plt.ylabel('calories')
plt.show()

# scatter plot
df.plot(x='fat', y='calories', kind='scatter', s=df.protein*100)
plt.title('calories vs. sugar')
plt.ylabel('calories')
plt.show()

# box plot for individual analysis
df.plot(y=['sugars', 'fat', 'sodium'], kind='box', subplots=True, grid=True)
plt.xlabel('calories')
plt.show()

# histograms
df.plot(y='sodium', kind='hist', bins=10, range=(50, 300))
plt.xlabel('')
plt.grid(True)
plt.show()

# other idioms
df.plot(kind='hist')
plt.show()

df.plot.hist()
plt.show()

df.hist(bins=20)
plt.show()

# plotting in subplots
fid, axes = plt.subplots(nrows=1, ncols=3)
df.plot(y='fat', kind='box', ax=axes[0])
df.plot(y='sugars', kind='box', ax=axes[1])
df.plot(y='sodium', kind='box', ax=axes[2])
axes[0].set_title('Fat')
axes[1].set_title('sugars')
axes[2].set_title('sodium')
plt.show()