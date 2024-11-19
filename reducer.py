#!/usr/bin/env python

import sys

total_price = 0
total_count = 0
price_squared_sum = 0

# Чтение данных от маппера
for line in sys.stdin:
    line = line.strip()
    price, count = map(float, line.split('\t'))
    
    total_price += price
    total_count += count
    price_squared_sum += price ** 2

# Вычисление среднего значения и дисперсии
if total_count > 0:
    average_price = total_price / total_count
    variance = (price_squared_sum / total_count) - (average_price ** 2)
    
    print(f"Average Price: {average_price}")
    print(f"Price Variance: {variance}")
else:
    print("No data to process.")