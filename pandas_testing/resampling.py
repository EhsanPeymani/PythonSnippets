import pandas as pd

data = pd.read_csv('weatherDataFixed.csv', index_col='timestamp', parse_dates=True)

# downsampling
# down sample to daily - daily mean value
daily_mean_temp = data['temp'].resample('D').mean()
print('--- daily_mean_temp ---')
print(daily_mean_temp)

# down sample to weekly and find max
weekly_max_temp = data.temp.resample('W').max()
print('--- weekly_max_temp: weeks end on Sunday ---')
print(weekly_max_temp)

# down sample to every 3 days and find min
every3D_min_temp = data.temp.resample('3D').min()
print('--- every3D_min_temp ---')
print(every3D_min_temp)

# up sample to every 15 minutes and forward fill
hourly_data = data.resample('15min').ffill()
print('--- every15min up sampling to have finer grids ---')
print(hourly_data.head(10))