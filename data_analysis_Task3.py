import pandas as pd

# Зчитуємо дані з Excel-файлу в DataFrame
file_path = 'Домашнє завдання_Data Analytics.xlsx'
data = pd.read_excel(file_path, sheet_name='Task3')

# Конвертуємо час початку події у формат datetime
data['ВРЕМЯ_НАЧАЛА_СОБЫТИЯ'] = pd.to_datetime(data['ВРЕМЯ_НАЧАЛА_СОБЫТИЯ'])

# Визначаємо флаг для подій, що стартують з 8:00 ранку
data['ЧАС_З_8_00'] = data['ВРЕМЯ_НАЧАЛА_СОБЫТИЯ'].dt.hour >= 8

# Групуємо дані за номером абонента та флагом часу
grouped_data = data.groupby(['НОМЕР_АБОНЕНТА', 'ЧАС_З_8_00'])

# Рахуємо сумарний використаний трафік за день для кожного абонента (в мегабайтах)
traffic_by_day = grouped_data['ИСПОЛЬЗОВАННЫЙ_ТРАФИК_ЗА_ДЕНЬ_KB'].sum().reset_index()
traffic_by_day['ИСПОЛЬЗОВАННЫЙ_ТРАФИК_ЗА_ДЕНЬ_MB'] = traffic_by_day['ИСПОЛЬЗОВАННЫЙ_ТРАФИК_ЗА_ДЕНЬ_KB'] / 1024

# Обчислюємо втрати для кожного абонента
traffic_by_day['ВТРАТИ'] = traffic_by_day['ИСПОЛЬЗОВАННЫЙ_ТРАФИК_ЗА_ДЕНЬ_MB'] - \
                           traffic_by_day.groupby('НОМЕР_АБОНЕНТА')['ИСПОЛЬЗОВАННЫЙ_ТРАФИК_ЗА_ДЕНЬ_MB'].shift(1, fill_value=0)

# Вартість 1 Мб GPRS Інтернету (у гривнях за 1 Мб)
cost_per_mb = 0.01

# Обчислюємо втрати в гривнях для кожного абонента
traffic_by_day['ВТРАТИ_ГРН'] = traffic_by_day['ВТРАТИ'] * cost_per_mb

# Рахуємо загальні втрати за весь період
total_losses = traffic_by_day['ВТРАТИ_ГРН'].sum()

print(f'Загальні втрати за період: {total_losses:.2f} грн')
