                                   #List Comprehensions
#1.	Сгенерировать список нечётных двузначных чисел.
odd_list = [number for number in range(1, 100) if number % 2 != 0]
print(odd_list)


#2.	Сгенерировать список из 10 чисел степени 2. От 1 до 10.
list_degrees = [number**2 for number in range (1, 10) ]
print(list_degrees)


#3.	Сгенерировать список всех трёхзначных чисел кратных 5 и 3.
multiples_5_and_3 = [number for number in range(100, 1000) if number % 5 == 0 or number % 3 == 0]
print(multiples_5_and_3)


#4.	Программа получает на вход три числа через пробел — начало и конец
#диапазона, а также степень, в которую нужно возвести каждое число из диапазона.
#Выведите числа получившегося списка через пробел.
start, stop, degree = map(int, input("Введите ваши три числа:").split())
range_in_degree = [number**degree for number in range (start,stop)]
print(range_in_degree)

                                     #Map, Filter, lambda
#5.	Числа вводятся в список в одной строке.
# #Отфильтровать список так, чтобы в нем остались числа, которые содержат цифру 0.
some_list = input('Введите ваши числа:').split()
list_0 = [number for number in some_list if "0" in number]
print(list_0)

#6.	Дан список состоящий из слов.
#Создать новый список и оставить строки в которых более двух символов 'a'
word_list = ["apple", "banana", "avocado", "grape", "anaconda", "kiwi", "mango"]
list_condition = [list for list in word_list if list.count('a') > 2]
print(list_condition)

#7.	Дан список, состоящий из строк. Сделать все строки в строки в верхнем регистре.
strings_list = ["hello", "world", "python", "programming", "openai"]
uppercased_list = list(map(lambda x: x.upper(), strings_list))
print(uppercased_list)






