# 2 Task

while True:
    try:
        number1 = float(input("\nВведіть перше число: "))
        number2 = float(input("\nВведіть перше число: "))\

        print("\nОберіть операцію:")
        print("1 — Додавання")
        print("2 — Віднімання")
        print("3 — Множення")
        print("4 — Ділення")
        print("5 — Піднесення до степеня")
        print("0 — Вихід")

        user_choice = int(input("\nВведіть операцію яку хчоете виконати: "))
    except ValueError:
        print("Ви не ввели ціле число.")
        continue

    try:
        if user_choice == 1:
            print(f"\n{number1 + number2}")

        elif user_choice == 2:
            print(f"\n{number1 - number2}")

        elif user_choice == 3:
            print(f"\n{number1 * number2}")

        elif user_choice == 4 and number2 % 2 != 0:
            print(f"\n{number1 / number2}")

        elif user_choice == 5:
            print(f"\n{number1 ** 2}")

        elif user_choice == 0:
            print("\nВи вийшли з калькулятору.")
            break

    except ValueError:
        print("\nВи ввели недійсну команду.")
        continue

# task 3


class Employee:
    def __init__(self, first_name: str, last_name: str, department: str, start_year: int):
        if not first_name or not last_name or not department:
            raise ValueError(
                "Ім'я, прізвище та відділ не можуть бути порожніми.")

        self.__first_name = first_name
        self.__last_name = last_name
        self.__department = department
        self.__start_year = start_year

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    @property
    def department(self):
        return self.__department

    @property
    def start_year(self):
        return self.__start_year

    def __str__(self):
        return f"{self.full_name}, Відділ: {self.department}, Початок роботи: {self.start_year}"


employees = []

while True:
    print("\n1 — Додати працівника")
    print("0 — Завершити введення")
    choice = input("Ваш вибір: ")

    if choice == "0":
        break
    elif choice == "1":
        try:
            fname = input("Ім'я: ")
            lname = input("Прізвище: ")
            dept = input("Відділ: ")
            year = int(input("Рік початку роботи: "))
            emp = Employee(fname, lname, dept, year)
            employees.append(emp)
        except ValueError as e:
            print(f"Помилка: {e}")
    else:
        print("Невірний вибір.")

print("\nПрацівники, прийняті після 2025 року:")
found = False
for emp in employees:
    if emp.start_year > 2025:
        print(emp)
        found = True

if not found:
    print("Немає таких працівників.")
