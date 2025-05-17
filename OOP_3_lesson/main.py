1


class Car:
    def __init__(self, make, model, year, color, mileage):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color
        self.__mileage = mileage

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    def get_mileage(self):
        return self.__mileage

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        if year > 1885:
            self.__year = year
        else:
            print("Некоректний рік випуску")

    def set_color(self, color):
        self.__color = color

    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage
        else:
            print("Пробіг не може бути від’ємним")

    def info(self):
        print(f"Марка: {self.__make}, Модель: {self.__model}, Рік: {self.__year}, "
              f"Колір: {self.__color}, Пробіг: {self.__mileage} км")


car = Car("Toyota", "Camry", 2015, "Червоний", 50000)
car.info()

print(car.get_model())

car.set_color("Синій")
car.set_mileage(52000)

car.info()

2


class English:
    def greeting(self):
        print("Hello, friend!")


class Spanish:
    def greeting(self):
        print("Hola, amigo!")


def hello_friend(lang1, lang2):
    lang1.greeting()
    lang2.greeting()


english = English()
spanish = Spanish()

hello_friend(english, spanish)

3


class Temperature:
    def __init__(self, temp_by_celsie: int):
        self.temp_by_celsie = temp_by_celsie

    def show_temperature(self):
        print(f"Температура надворі зараз {self.temp_by_celsie} градусів °C.")

    @classmethod
    def faringate_temp(cls, temp_by_faringate: int):
        temp = temp_by_faringate + 97, 88
        print(f"Температура надворі сягає {temp} °F")


temp1 = Temperature(20)
temp1.show_temperature()

temp2 = Temperature.faringate_temp(30)
