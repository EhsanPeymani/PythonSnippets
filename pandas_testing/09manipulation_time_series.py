import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('weatherDataFixed.csv', parse_dates=['timestamp'])


# i will add week day name as a column to have a string type
data['DayName'] = data['timestamp'].dt.weekday_name
print('---- Day Name ----')
print(data.head(2))

# manipulating DayName: Take the first 3 letter and make it uppercase
data['DayNameShort'] = data['DayName'].str.slice(0,3).str.upper()
print('---- Short Day Name ----')
print(data.head(2))

# counting the number of records for sundays
c = data['DayNameShort'].str.contains('SUN').sum()
print('---- ---------------- ----')
print('The number of records on Sunday: ', c)

# localizing the time - time zone aware
data_NO = data.copy()
data_NO['timestamp'] = data_NO['timestamp'].dt.tz_localize('Europe/Oslo')
print('---- Localize to Oslo Time ----')
print(data_NO.head(2))

# convert timezone to Tehran time
data_Tehran = data_NO.copy()
data_Tehran['timestamp'] = data_Tehran['timestamp'].dt.tz_convert('Asia/Tehran')
print('---- Convert Timezone to Tehran Time ----')
print(data_Tehran.head(2))

# One day has 24 samples
data.set_index(inplace=True, keys=['timestamp'])
day1 = data['2018-06-15 00:00':'2018-06-15 01:00']
day1 = day1.resample('15min').first().interpolate(method='linear')
print('---- Upsampled to every 15 min ----')
print(day1)
day1.plot()
plt.show()

