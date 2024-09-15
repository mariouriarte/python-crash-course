from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

#path = Path('weather_data/sitka_weather_07-2021_simple.csv')
path = Path('weather_data/sitka_weather_2021_simple.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row  = next(reader)
# print(header_row)
# for index, column_header in enumerate(header_row):
#     print(index, column_header)
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(current_date)
    high = int(row[4])
    highs.append(high)
    low = int(row[5])
    lows.append(low)

print(highs)

plt.style.use('tableau-colorblind10')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')

# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()