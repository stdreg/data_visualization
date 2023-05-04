import csv
from datetime import datetime
import matplotlib.pyplot as plt

with open("produkt_klima_tag_19500101_20211231_00403.txt") as file:
    reader = csv.reader(file,delimiter=';')
    header_row = next(reader)
    for index, header in enumerate(header_row):
        print(f"{index} {header}")

    highs, lows, dates = [], [], []    
    for row in reader:
        date = datetime.strptime(row[1],'%Y%m%d')
        high = float(row[15])
        low = float(row[16])
        highs.append(high)
        lows.append(low)
        dates.append(date)

#print(highs)        
plt.style.use("seaborn")
fig, plot = plt.subplots()
plot.plot(dates, highs, c='red', alpha=0.5)
plot.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title("High- and low temperatures in Berlin-Dahlem", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
