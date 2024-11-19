#!/usr/bin/env python

import sys

# Чтение данных из стандартного ввода
for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    
    # Предполагаем, что цена находится в определенном столбце, например, в 10-м
    try:
        price = float(fields[9])  # Замените 9 на индекс столбца с ценой
        print(f"{price}\t1")
    except (ValueError, IndexError):
        continue