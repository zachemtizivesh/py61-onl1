
#1. Напишите функцию minimum вычисляющую минимум двух чисел.
def calculate_minimum(number1,number2,*args):
    print(min(number1,number2))

#number1 = int(input('Введите ваше первое число: '))
#number2 = int(input('Введите ваше второе число: '))

#2.	Найдите минимальное четырёх чисел с помощью функции написанной в предыдущей задаче.
#Новую функцию не создавать! Использовать функцию из предыдущей задачи!
calculate_minimum(5,6,2,4)

#3.	Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
#вычисляющую расстояние между точкой (x1, y1) и (x2, y2).
#Считайте четыре действительных числа и выведите результат работы этой функции.

#4.	Дано натуральное число number > 1.
#Проверьте, является ли оно простым.
#Программа должна вывести слово YES, если число простое и NO, в противном случае
def prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
number = int(input('Введите натуральное число больше 1: '))
if prime_number(number):
    print("YES")
else:
    print("NO")


#5.	Напишите функцию fibbonachi которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
#Ищем число Фиббоначи через цикл! Рекурсию не использовать!
def fibonacci_number(n):
    if n < 0:
        raise ValueError("n должно быть неотрицательным целым числом.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
n = int(input("Введите неотрицательное целое число n: "))
result = fibonacci_number(n)
print(f"{n}-е число Фибоначчи равно: {result}")

