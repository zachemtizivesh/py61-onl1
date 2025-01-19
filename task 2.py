
#1)	Напишите программу, которая проверяет последнюю цифру числа.
#Если последняя цифра числа 3, то вывести True иначе вывести False.
numbers =input("Введите любое число: ")
last_digit = numbers[-1]
if last_digit == "3":
    print(True)
else:
    print(False)


#2)	Напишите программу, которая выводит True, если хотя бы одно из чисел number_1,
# number_2, number_3 отрицательно.
#Если нет вывести False. Числа вводятся с клавиатуры в одной строке.
number_1, number_2, number_3 = map(int, input("Введите три числа:").split())
if number_1 < 0 or number_2 < 0 or number_3 < 0:
    print(True)
else:
    print(False)


#3)	Верно ли что, целые number_1, number_2 имеют одинаковую четность.
number_1, number_2 = map(int,input("Введите два целых числа: ").split())
if (number_1 % 2) == (number_2 % 2):
    print(True)
else:
    print(False)



#4)	Даны три стороны треугольника side_a, side_b, side_c.
#Выведите equilateral если треугольник равносторонний, isosceles если равнобедренный и scalene если разносторонний
side_a, side_b, side_c = map(int, input("Введите три числа:").split())
if side_a == side_b == side_c:
    print('equilateral')
elif side_a ==side_b or side_a == side_c or side_c == side_b:
    print('isosceles')
else:
    print("scalene")


#5)	Найти количество четных чисел среди заданных трех целых чисел.
#В ответе вывести количество четных чисел.
number_1, number_2, number_3 = map(int, input("Введите три числа:").split())
even_count = 0
if number_1 % 2 == 0:
    even_count += 1
if number_2 % 2 == 0:
    even_count += 1
if number_3 % 2 == 0:
    even_count += 1
print(even_count)


#6)	Дано двузначное число. Определить является ли сумма его цифр двузначным числом.
number = input("Введите двухзначное число: ")
if len(number) == 2 and number.isdigit():
    tens = int(number[0])
    units = int(number[1])
    sum_of_digins = tens + units
    if 10 <= sum_of_digins <= 99:
        print('Сумма цифр вашего числа является двухзначным числом')
    else:
        print('Сумма цифр вашего числа не является двухзначным числом')
else:
    print("Введенное вами число не является двухзначным")


#7)	Дано четырёхзначное число. Проверить, одинаковы ли все цифры в нём.
number = input("Введите четырёхзначное число:")
if len(number) == 4 and number.isdigit():
    thousands = int(number[0])
    hundreds = int(number[1])
    tens = int(number[2])
    units = int(number[3])
    if thousands == hundreds == tens == units:
        print("В вашем числе 4 одинаковые цифры")
    else:
        print("В вашем числе не все 4 цифры одинаковы")
else:
    print("Вы ввели не 4-х значное число")


#8)	Напишите программу, принимающую на вход год и выводящую "Високосный",
#если в этом году действительно 366 дней, и "Не високосный" иначе.
#Год считается високосным, если его номер делится на 4, но не делится на 100 или же делится на 400.
numbers_god = int(input("Введите любой год: "))
if (numbers_god % 4 == 0 and numbers_god % 100 != 0) or numbers_god % 400 == 0:
    print('Введённый вами год является високосным')
else:
    print("Ваш год не является високосным")



               #Цикл For задачи с числами.
#9)	Вывести на экран число "10" 20 раз столбиком.
for a in range(20):
    print(10)


#10)	Даны два числа start и stop. Составить программу вывода на экран всех чисел от start до stop.
start = int(input(f" Введите первое число"))
stop = int(input(f" Введите второе число"))
for number in range(start, stop + 1):
    print(number)

#11)Выведите на экран в одну строку числа от 100 до -100 включительно.
numbers = []
for i in range(100, -101, -1):
    numbers.append(str(i))
print(' '.join(numbers))


#12)Найти сумму всех целых чисел от 100 до 500 включительно.
total = 0
for number in range(100, 501):
    total += number
print(total)


#13)Найти произведение всех целых чисел от 5 до 20 включительно.
total = 1
for number in range(5, 21):
    total *= number
print(total)


#14)Дано натуральное число n. Вывести на экран факториал этого числа.
#Например: 5! = 1 * 2 * 3 * 4 * 5 = 120
factorial = 1
number = int(input(f"Введите ваше число: "))
for number in range(1, number + 1):
    factorial *= number
print(factorial)