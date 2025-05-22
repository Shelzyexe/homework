# Task 2
class Contact:
    def __init__(self, surname: str, name: str, age: int, mob_phone: int, email: str):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f"Name: {self.name}, phone number: {self.mob_phone}"

    def sent_message(self):
        print(f"Message has been sent to {self.name}, on {self.email}.")


class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job: str):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        return f"{self.name} ({self.job}) — reachable at {self.email}"\



contact1 = Contact("Shevchenko", "Taras", 30,
                   380501234567, "taras@example.com")
contact2 = UpdateContact("Franko", "Ivan", 45,
                         380987654321, "ivan@example.com", "Writer")

print("contact1.__dict__:", contact1.__dict__)
print("contact2.__dict__:", contact2.__dict__)
print("UpdateContact.__base__:", UpdateContact.__base__)
print("Contact.__bases__:", Contact.__bases__)

# # Task 3
setattr(contact1, "expirience", 12)

print(contact1.expirience)
print(hasattr(contact2, "expirience"))

delattr(contact1, "expirience")
print(hasattr(contact1, "expirience"))

print(getattr(contact1, "name"))

# Task 4

c1 = Contact("Shevchenko", "Taras", 30, 380501234567, "taras@example.com")
c2 = Contact("Kotsiubynsky", "Mykhailo", 35,
             380503456789, "mykhailo@example.com")

uc1 = UpdateContact("Franko", "Ivan", 45, 380987654321,
                    "ivan@example.com", "Writer")
uc2 = UpdateContact("Lesya", "Ukrainka", 40, 380931112233,
                    "lesya@example.com", "Poet")

print(isinstance(c1, Contact))
print(isinstance(c1, UpdateContact))
print(isinstance(uc1, Contact))
print(isinstance(uc1, UpdateContact))

print(issubclass(UpdateContact, Contact))
print(issubclass(Contact, UpdateContact))

# Task 5

print("ДО ВИДАЛЕННЯ job")
print("Contact.__dict__:", Contact.__dict__)
print("UpdateContact.__dict__:", UpdateContact.__dict__)
print("c1.__dict__:", c1.__dict__)
print("uc1.__dict__:", uc1.__dict__)

del uc1.job

print("\n== ПІСЛЯ ВИДАЛЕННЯ job ==")
print("Contact.__dict__:", Contact.__dict__)
print("UpdateContact.__dict__:", UpdateContact.__dict__)
print("c1.__dict__:", c1.__dict__)
print("uc1.__dict__:", uc1.__dict__)

try:
    print(uc1.get_message())
except AttributeError as e:
    print("ПОМИЛКА при виклику get_message:", e)

# Task 6

print("ВСІ атрибути класу Contact:")
print(dir(Contact))

print("\nВСІ атрибути класу UpdateContact:")
print(dir(UpdateContact))
