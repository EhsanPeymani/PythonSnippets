import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('weatherDataFixed.csv', index_col='timestamp', parse_dates=True)


# rolling average - moving average for 24 samples
temperature = data['temp']
temperature_avg = temperature.rolling(window=24).mean()

df = pd.DataFrame({'temp':temperature, 'temp_avg':temperature_avg})
df.plot()
plt.title('Effect of Moving Average with 24 samples (24 hours)')
plt.grid()
plt.show()