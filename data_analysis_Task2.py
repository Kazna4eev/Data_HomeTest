import pandas as pd
import matplotlib.pyplot as plt

# Зчитуємо дані з Excel-файлу в DataFrame
file_path = 'Домашнє завдання_Data Analytics.xlsx'
data = pd.read_excel(file_path, sheet_name='Task2')

# Зробимо групування за часом сутності та порахуємо кількість недовантажених записів для кожного дня
rejected_by_time = data[data['rejected'] == 1].groupby(pd.Grouper(key='event_starttime', freq='D')).size()

# Побудуємо графік для візуалізації залежності між часом та ймовірністю недовантаження
plt.figure(figsize=(12, 6))
plt.plot(rejected_by_time.index, rejected_by_time.values, marker='o', linestyle='-', color='red')
plt.xlabel('Дата')
plt.ylabel('Кількість недовантажених записів')
plt.title('Динаміка недовантажених записів за дні')
plt.grid(True)
plt.show()

# Дослідження залежності між різними стовпцями та rejected
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.scatter(data['cost'], data['rejected'], alpha=0.3, color='blue')
plt.xlabel('Вартість')
plt.ylabel('rejected')
plt.title('Залежність між вартістю та rejected')

plt.subplot(2, 2, 2)
plt.scatter(data['duration'], data['rejected'], alpha=0.3, color='green')
plt.xlabel('Тривалість')
plt.ylabel('rejected')
plt.title('Залежність між тривалістю та rejected')

plt.subplot(2, 2, 3)
data.groupby('service_id')['rejected'].mean().plot(kind='bar', color='orange')
plt.xlabel('service_id')
plt.ylabel('Середній rejected')
plt.title('Середній rejected за service_id')

plt.subplot(2, 2, 4)
data.groupby('tarrif_plan_id')['rejected'].mean().plot(kind='bar', color='purple')
plt.xlabel('tarrif_plan_id')
plt.ylabel('Середній rejected')
plt.title('Середній rejected за tarrif_plan_id')

plt.tight_layout()
plt.show()
