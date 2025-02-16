                #1. Класс-итератор RangeSquared

class RangeSquared:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            square = self.current ** 2
            self.current += 1
            return square
        else:
            raise StopIteration



                 #2. Генератор factorial_gen

def factorial_gen(n: int):
    factorial = 1
    for i in range(n + 1):
        if i == 0:
            yield factorial
        else:
            factorial *= i
            yield factorial



        #3 Генератор read_file_lines

def read_file_lines(filename: str):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()  # Убираем символы новой строки



                    #4. Исправление кода в соответствии с принципом KISS

def calculate_complex_formula(a, b, c, d, e, f, g, h):
    result = 0
    if a > 0:
        result += b * c
    else:
        result -= d / e
    if g < h:
        result += f * (g + h)
    else:
        result -= (d - f) / g
    return result