import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np_rand

data = pd.read_csv('weatherDataFixed.csv', parse_dates=['timestamp'], index_col='timestamp')
perc = np_rand.randint(0, 12, len(data))
data['nperc'] = perc

# plot a time series
data['temp'].plot(title='Temperature in June')
plt.ylabel('Celcius')
plt.show()

# plot multiple series
data[['temp', 'nperc']].plot()
plt.show()

# plot multiple series
data[['temp', 'nperc']].plot(subplots=True)
plt.show()

# plot multiple series
fid, axes = plt.subplots(nrows=2, ncols=1)
data['temp'].plot(ax=axes[0], title='Temperature')
data['nperc'].plot(ax=axes[1], title='Percipitation')
axes[0].set_ylabel('Celcius')
axes[1].set_ylabel('mm')
axes[0].set_xlabel('') # removing xlabel
axes[0].tick_params(axis='x',
                    which='both',
                    bottom=False,
                    top=False,
                    labelbottom=False)
plt.show()