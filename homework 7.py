# 1. Создать файл input.txt и записать в него 10 чисел через пробел. Числа хранятся в списке numbers
# записываем наш список
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Открываем файл для записи
with open('input.txt', 'w') as file:
    file.write(' '.join(map(str, numbers)))
print("Числа записаны в ваш файл ")


# 2. Считать из файла input.txt эти числа. Затем записать их произведение в файл output.txt.
# Читаем числа из файла input.txt
with open('input.txt', 'r') as file:
    numbers = list(map(int, file.read().strip().split()))
# Вычисляем произведение чисел
product = 1
for number in numbers:
    product *= number
with open('output.txt', 'w') as file:
    file.write(str(product))
print("Произведение чисел записано в файл output.txt.")

import json

data = {
    12345: ("Alice", 30),
    23456: ("Bob", 25),
    34567: ("Charlie", 35),
    45678: ("Diana", 28),
    56789: ("Ethan", 40)
}


#3.	Список товаров, имеющихся на складе, включает в себя наименование товара, количество единиц товара,
#цену единицы и дату поступления товара на склад.
#Вывести список товаров, хранящихся больше месяца и стоимость которых превышает 1 000 000 р.
from datetime import datetime, timedelta
products = [
     {"name": "Table", "quantity": 100, "price_per_unit": 450, "arrival_date": "10.09.2024"},
     {"name": "Board", "quantity": 1000, "price_per_unit": 2590, "arrival_date": "28.12.2024"},
     {"name": "Chair", "quantity": 800, "price_per_unit": 2500, "arrival_date": "12.01.2025"},
 ]


def filter_products(products):
     current_date = datetime.now()
     filtered_products = []
     for product in products:
         arrival_date = datetime.strptime(product["arrival_date"], "%d.%m.%Y")
         total_value = product["quantity"] * product["price_per_unit"]
         # Проверяем условия: хранился больше месяца и стоимость больше 1 000 000
         if (current_date - arrival_date) > timedelta(days=30) and total_value > 1000000:
             filtered_products.append(product)
     return filtered_products
#Получаем отфильтрованный список товаров.
filtered_products = filter_products(products)
 # Выводим результат
if filtered_products:
     print("Товары, хранящиеся больше месяца и стоимость которых превышает 1 000 000 р.:")
     for product in filtered_products:
         print(f"Наименование: {product['name']}, Количество: {product['quantity']}, "
               f"Цена за единицу: {product['price_per_unit']}, "
               f"Дата поступления: {product['arrival_date']}")
else:
     print("Нет товаров, соответствующих критериям.")


#5.	Создать словарь в качестве ключа которого будет 5 значное число,
#а в качестве значений кортеж состоящий из 2 элементов – имя(str) и возраста(int).
#Сделать 5-6 элементов словаря и записать данный словарь на диск в файл json формата
# Создание словаря
data = {
    12345: ("Alice", 30),
    23456: ("Bob", 25),
    34567: ("Charlie", 35),
    45678: ("Diana", 28),
    56789: ("Ethan", 40)
}
# Преобразование словаря для записи в JSON
# В JSON нельзя напрямую записывать кортежи, поэтому преобразуем их в списки
json_data = {key: list(value) for key, value in data.items()}
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)
print("Данные успешно записаны в файл data.json.")


#6.	Прочитать сохранённый json – файл и записать данные на диск в csv файл.
#Первое значение каждой строки должно начинаться со слова person, значения разделить ;
import json
import csv

with open('data.json', 'r', encoding='utf-8') as json_file:
     json_data = json.load(json_file)
 # Запись данных в CSV-файл
with open('data.csv', 'w', newline='', encoding='utf-8') as csv_file:
     csv_writer = csv.writer(csv_file, delimiter=';')
     # Запись заголовка (если необходимо)
     csv_writer.writerow(['ID', 'Name', 'Age'])
     # Запись данных
     for key, value in json_data.items():
         # Добавляем "person" перед ID
         row = [f'person {key}', value[0], value[1]]
         csv_writer.writerow(row)
print("Данные успешно записаны в файл data.csv.")