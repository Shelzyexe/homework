1

while True:
    userkey = input("Введіть свій ключ: ")
    if len(userkey) == 8:
        print("Дякуємо, ви ввійшли в систему.")
        break
    else:
        print("Ви ввели щось не те, цифр або символів повинно бути 8.")

pro_editor_key = "12031392"


class Editor:
    def __init__(self, document: str):
        self.document = document

    def view_document(self):
        return f"Ось ваш документ, {self.document}, ви ввійшли під ключем {userkey}"

    def edit_document(self):
        return f"Редагування документів недоступне для безкоштовної версії, перейдіть на план підписки."

    def __str__(self):
        return self.view_document()


class ProEditor(Editor):
    def edit_document(self):
        return f"Вам доступне редагування документів, з чого почнемо?"

    def __str__(self):
        return super().__str__()


if userkey == pro_editor_key:
    current_editor = ProEditor
else:
    current_editor = Editor

doc1 = current_editor("Document 1")
doc2 = current_editor("Document 2")

print(doc1.view_document())
print(doc2.edit_document())


# 3
# # Створіть ієрархію класів із використанням множинного успадкування.
# # Виведіть на екран порядок вирішення методів для кожного класу. Поясніть, чому лінеаризація даних класів виглядає саме так.

# class MobilePhone:
#     def __init__(self,name_phone:str, model: str, cameras_pixels: int, screen_size: int, color: str, battery_size: int):
#         self.cameras_pixels = cameras_pixels
#         self.screen_size = screen_size
#         self.color = color
#         self.battery_size = battery_size
#         self.model = model
#         self.name_phone = name_phone

#     def info_about_phone(self):
#         print(f"Name of the phone : {self.name_phone}"
#               f"Cameras pixels in phone : {self.cameras_pixels}"
#               f"Screen size : {self.screen_size}"
#               f"Color of the phone : {self.color}"
#               f"Battery size : {self.battery_size}")

# class Iphone(MobilePhone):
#     def __init__(self, name_phone, model, cameras_pixels, screen_size, color, battery_size, ios_version: int):
#         super().__init__(name_phone, model, cameras_pixels, screen_size, color, battery_size)
#         self.ios_version = ios_version

#     def info_about_phone(self):
#         print(f"Name of the phone : {self.name_phone}"
#             f"Cameras pixels in phone : {self.cameras_pixels}"
#             f"Screen size : {self.screen_size}"
#             f"Color of the phone : {self.color}"
#             f"Battery size : {self.battery_size}"
#             f"Ios version : {self.ios_version}")


7


class Transport:
    def __init__(self, brand: str, model: str, year: int, max_speed: int, hp: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.hp = hp

    def show_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Максимальна швидкість: {self.max_speed} км/год")
        print(f"Кількість кінських сил: {self.hp} hp")


class Car(Transport):
    def __init__(self, brand, model, year, max_speed, hp, num_doors: int,
                 tires_brand: str, car_color: str, engine_type: str, gas_type: str):
        super().__init__(brand, model, year, max_speed, hp)
        self.num_doors = num_doors
        self.tires_brand = tires_brand
        self.car_color = car_color
        self.engine_type = engine_type
        self.gas_type = gas_type

    def show_info(self):
        super().show_info()
        print(f"Кількість дверей: {self.num_doors}")
        print(f"Виробник шин: {self.tires_brand}")
        print(f"Колір машини: {self.car_color}")
        print(f"Тип двигуна: {self.engine_type}")
        print(f"Тип палива: {self.gas_type}")
        print("-" * 40)


class Airplane(Transport):
    def __init__(self, brand, model, year, max_speed, hp,
                 wing_span: int, engine_count: int, gas_type: str, passengers_count: int):
        super().__init__(brand, model, year, max_speed, hp)
        self.wing_span = wing_span
        self.engine_count = engine_count
        self.gas_type = gas_type
        self.passengers_count = passengers_count

    def show_info(self):
        super().show_info()
        print(f"Розмах крил: {self.wing_span} м")
        print(f"Кількість двигунів: {self.engine_count}")
        print(f"Тип палива: {self.gas_type}")
        print(f"Кількість пасажирів: {self.passengers_count}")
        print("-" * 40)


car1 = Car("Toyota", "Camry", 2020, 220, 180, 4,
           "Michelin", "Синій", "Бензиновий", "АІ-95")
car2 = Car("BMW", "M5", 2022, 280, 600, 4, "Pirelli",
           "Чорний", "Бензиновий", "АІ-98")

plane1 = Airplane("Boeing", "737", 2015, 850, 24000, 35, 2, "Керосин", 180)
plane2 = Airplane("Airbus", "A320", 2018, 830, 26000, 34, 2, "Керосин", 170)


def show_all_info(obj: Transport):
    obj.show_info()


show_all_info(car1)
show_all_info(car2)
show_all_info(plane1)
show_all_info(plane2)
