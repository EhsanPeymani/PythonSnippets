import pandas as pd

# creating dataframe from dictionary
data = {'weekday':['mon', 'wed', 'fri'],
        'units':[12, 33, 15],
        'hours':[421, 534, 775]}

data_df = pd.DataFrame(data)
print(data_df)

# crating dataframe using lists
weekdays = ['mon', 'wed', 'fri']
units = [12, 33, 15]
hours = [421, 534, 775]

labels = ['weekdays', 'units', 'hours']
data = [weekdays, units, hours] #list of lists
zipped = zip(labels, data)

dict_data = dict(zipped) # this renders data as dictionary in the previous section

data_df = pd.DataFrame(dict_data)
print(data_df)

# broadcasting
# adding a new column to the dataframe by one scalar
data_df['location'] = 'NO'
print(data_df)

# broadcasting
# adding new columns in the dict
dict_data['location'] = 'US'
new_data_df = pd.DataFrame(dict_data)
print(new_data_df)