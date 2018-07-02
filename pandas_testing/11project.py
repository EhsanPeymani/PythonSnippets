import pandas as pd
import matplotlib.pyplot as plt

# reading data with no header
df = pd.read_csv('austin_weather.txt', header=None)

# adding headers
headers     = 'Wban,date,Time,StationType,sky_condition,sky_conditionFlag,visibility,visibilityFlag,' \
              'wx_and_obst_to_vision,wx_and_obst_to_visionFlag,dry_bulb_faren,dry_bulb_farenFlag,' \
              'dry_bulb_cel,dry_bulb_celFlag,wet_bulb_faren,wet_bulb_farenFlag,wet_bulb_cel,wet_bulb_celFlag,' \
              'dew_point_faren,dew_point_farenFlag,dew_point_cel,dew_point_celFlag,relative_humidity,' \
              'relative_humidityFlag,wind_speed,wind_speedFlag,wind_direction,wind_directionFlag,' \
              'value_for_wind_character,value_for_wind_characterFlag,station_pressure,station_pressureFlag,' \
              'pressure_tendency,pressure_tendencyFlag,presschange,presschangeFlag,sea_level_pressure,sea_level_pressureFlag,' \
              'record_type,hourly_precip,hourly_precipFlag,altimeter,altimeterFlag,junk'

header_list = headers.split(',')
df.columns = header_list

# dropping columns that are not of our interest
cols_to_drop = ['sky_conditionFlag',
 'visibilityFlag',
 'wx_and_obst_to_vision',
 'wx_and_obst_to_visionFlag',
 'dry_bulb_farenFlag',
 'dry_bulb_celFlag',
 'wet_bulb_farenFlag',
 'wet_bulb_celFlag',
 'dew_point_farenFlag',
 'dew_point_celFlag',
 'relative_humidityFlag',
 'wind_speedFlag',
 'wind_directionFlag',
 'value_for_wind_character',
 'value_for_wind_characterFlag',
 'station_pressureFlag',
 'pressure_tendencyFlag',
 'pressure_tendency',
 'presschange',
 'presschangeFlag',
 'sea_level_pressureFlag',
 'hourly_precip',
 'hourly_precipFlag',
 'altimeter',
 'record_type',
 'altimeterFlag',
 'junk']

df = df.drop(cols_to_drop, axis='columns')

# assigning timestamp
# date and Time columns are of type int64
df['date'] = df['date'].astype(str) # making date columns to string
df['Time'] = df['Time'].apply(lambda x: '{0:0>4}'.format(x)) # adding leading zeros to the string
datetimes_string = df['date'] + df['Time']
datetimes = pd.to_datetime(datetimes_string, format='%Y%m%d%H%M')
df.set_index(datetimes, inplace=True)
print(df.head(2))

# Converting to numeric values, non numerics shall be NaN
df['dry_bulb_faren'] = pd.to_numeric(df['dry_bulb_faren'], errors='coerce')
df['wind_speed'] = pd.to_numeric(df['wind_speed'], errors='coerce')
df['dew_point_faren'] = pd.to_numeric(df['dew_point_faren'], errors='coerce')
df['visibility'] = pd.to_numeric(df['visibility'], errors='coerce')

# find largest difference between temperatures in sunny and overcast days
sunny = df['sky_condition'] == 'CLR'
overcast = df['sky_condition'].str.contains('OVC')

max_temp_sunny = df.loc[sunny, 'dry_bulb_faren'].resample('D').max()
max_temp_overcast = df.loc[overcast, 'dry_bulb_faren'].resample('D').max()

diff = max_temp_sunny.mean() - max_temp_overcast.mean()
print('Max diff of temperature: ', diff)

# is there correlation between Temprerature and Visibility
mean_weekly_df = df[['visibility', 'dry_bulb_faren']].resample('W').mean()

print('Pearson\'s correlation between Visibility and Temperature')
print(mean_weekly_df.corr())

mean_weekly_df.plot(subplots=True)
plt.show()

# heat or humidity
heat_humidity_df = df[['dew_point_faren', 'dry_bulb_faren']].resample('M').max()
heat_humidity_df.corr()
heat_humidity_df.plot(subplots=True, kind='hist', bins=10)
plt.show()