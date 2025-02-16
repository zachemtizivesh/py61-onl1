class BankAccount:
    def __init__(self, balance:float=0):
        self.__balance = balance #Создание атрибута для хранения баланса
        self.daily_limit = 5000  #Лимит снятия за день
        self.withdrawals_today = 0 #Кол-во снятий за сегодня
        self.max_withdrawals = 3  #Максимальное кол-во снятий за день

    def deposit(self, amount: float):
      #Пополнение счёта
        if amount <= 0:
            print('Счет должен быть положительным') #Проверка есть ли на счету деньги
        self.__balance += amount
        print(f'На счет добавлено {amount}. Сейчас на балансе: {self.__balance}')

    def withdraw(self, amount: float):
               #Метод для снятия денег со счёта
        if amount <= 0:
            print("Сумма депозита должна быть положительной.")
            return

        if self.withdrawals_today >= self.max_withdrawals:
            print("Превышено кол-во снятий за сегодня.")
            return
        if amount > self.__balance: # Проверка хватает ли денег для снятия
            print("Недостаточно денег на счету")
            return
        if amount > self.daily_limit:
            print(f"Превышено максимальный лимит снятия за день в  {self.daily_limit}. ")
            return
        if amount > self.__balance:
            print("Нет денег на счету")
            return
        self.__balance -= amount
        self.withdrawals_today += 1
        print(f"Со счета снято {amount}. Текущий баланс: {self.__balance}")

    def get_balance(self):
        # Метод для получения текущего баланса
        return self.__balance

    def reset_withdrawals(self):
        # Метод для сброса кол-ва снятий за сегодня
        reset_withdrawals_today = 0



import time

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.hunger = 100  # 100 - сыт, 0 - голоден

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

    def eat(self, amount: int):
        self.hunger = min(100, self.hunger + amount)
        print(f"{self.name} has eaten. Hunger level is now {self.hunger}")

    def decrease_hunger(self):
        if self.hunger > 0:
            self.hunger -= 10
            print(f"{self.name}'s hunger level is now {self.hunger}")
        if self.hunger <= 30:
            print(f"{self.name} is getting hungry!")

class Lion(Animal):
    def make_sound(self):
        return "Roar!"

    def hunt(self):
        return f"{self.name} is hunting!"

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"

    def trumpet(self):
        return f"{self.name} is trumpeting!"

class Penguin(Animal):
    def make_sound(self):
        return "Quack!"

    def swim(self):
        return f"{self.name} is swimming!"

# Словарь с данными о животных
animal_data = {
    "Коко": 3,  # Пингвин
    "Симба": 5,  # Лев
    "Думбо": 8   # Слон
}




class Temperature:
    def __init__(self, celsius: float):
        self._celsius = None
        self.celsius = celsius  # Используем сеттер для проверки

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже -273.15°C")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return (self._celsius * 9/5) + 32

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

# Пример использования:
try:
    temp = Temperature(25)  # Создаем объект с температурой 25°C
    print(f"Температура в Цельсиях: {temp.celsius}°C")
    print(f"Температура в Фаренгейтах: {temp.fahrenheit}°F")
    print(f"Температура в Кельвинах: {temp.kelvin}K")

    temp.celsius = -300  # Попытка установить недопустимую температуру
except ValueError as e:
    print(e)

temp.celsius = 0  # Устанавливаем допустимую температуру
print(f"Температура в Цельсиях: {temp.celsius}°C")
print(f"Температура в Фаренгейтах: {temp.fahrenheit}°F")
print(f"Температура в Кельвинах: {temp.kelvin}K")