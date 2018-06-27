import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cereal.csv', index_col='name')

features = ['calories', 'protein', 'fat', 'sodium', 'sugars']
df = df[features]

# step 1 - use describe()
print(df.describe())

# these all ignore null entries
# count()
# mean()
# std()
# median()
# quantile(q)
# min()
# max()
