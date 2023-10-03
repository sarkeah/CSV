import csv
from datetime import datetime
import matplotlib.pyplot as plt


def read_data_from_file(f_name):  # отдельная процедура для чтения файла
    tmp_dates, tmp_highs, tmp_lows = [], [], []  # списки с датами, самыми высокими и самыми низкими температурами
    with open(f_name) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            try:
                cur_date = datetime.strptime(row[2], '%Y-%m-%d')
                high = (int(row[8]) - 32) * 5 / 9
                low = (int(row[9]) - 32) * 5 / 9  # приводим дату и температуры к валидным значениям
            except ValueError:
                print(cur_date, 'have no data about date, low temperature or high temperature')
            else:
                tmp_dates.append(cur_date)
                tmp_highs.append(high)
                tmp_lows.append(low)
    return tmp_dates, tmp_highs, tmp_lows


file_name = 'sitka_weather_2018_full.csv'
dates, highs, lows = read_data_from_file(file_name)

fig = plt.figure(dpi=128, figsize=(10, 6))  # создание диаграммы
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='purple', alpha=0.3)
plt.title('Температура в 2018-2019 годax. город Ситка')
plt.ylabel('температура', fontsize=15)
plt.xlabel('', fontsize=10)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=20)
plt.show()
