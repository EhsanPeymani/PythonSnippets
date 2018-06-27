import pandas as pd

# reading CSV and parsing timestamps
data = pd.read_csv('weatherData.csv', skiprows=11, delimiter=';',
                   infer_datetime_format=True,
                   parse_dates={'timestamp':[0,1,2,3,4]},
                   usecols=[0,1,2,3,4,5,6])

# fixing timestamp column -convert to pandas datetime object
data.timestamp = pd.to_datetime(data.timestamp, format='%Y %m %d %H %M')

# making ts as index
data.set_index('timestamp', inplace=True)

# improving column names
data.columns = ['temp', 'percip']

print('---------------- data dataframe ----------------')
print(data.head(2))

print('---------------- data info() ----------------')
print(data.info())

print('---------------- data for 2018-06-20 ----------------')
print(data['2018-06-20'])

print('---------------- data for 2018-06-20 beween 18 to 24 ----------------')
print(data['2018-06-20 18:00:00':'2018-06-20 23:59:00'])

print('---------------- asking data for 2018-June-15 ----------------')
print(data['2018-June-15'])

# data for 2018-June-15 16:00 to 17:00
data_06_15 = data['2018-June-15 16:00:00':'2018-June-15 17:00:00']
new_sample_ts = pd.to_datetime(['2018-June-15 16:00:00','2018-June-15 16:20:00','2018-June-15 16:40:00','2018-June-15 17:00:00'])

new_data_06_15 = data_06_15.reindex(new_sample_ts)
print('---------------- reindex: data for 2018-June-15 16:00 to 17:00 ----------------')
print(new_data_06_15)

new_data_06_15 = data_06_15.reindex(new_sample_ts, method='ffill')
print('---------------- reindex: data for 2018-June-15 16:00 to 17:00 with Forward Filling ----------------')
print(new_data_06_15)

new_data_06_15 = data_06_15.reindex(new_sample_ts, fill_value=-1)
print('---------------- reindex: data for 2018-June-15 16:00 to 17:00 filling values with -1 ----------------')
print(new_data_06_15)

