from datetime import date


class MyClass1:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        age = date.today().year - birthYear
        return cls(surname, name, age)

    @staticmethod
    def chack_age(age):
        if age >= 18:
            return True
        else:
            return False

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))


class MyClass2(MyClass1):
    def __init__(self, surname, name, age):
        super().__init__(surname, name, age)

    @classmethod
    def counter_ages(cls, people):
        count = 0
        for person in people:
            if cls.chack_age(person.age):
                count += 1
        print(f"\nКількість людей, які досягли повноліття: {count}")


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan',  2000)
m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2000)

m_per1.print_info()
m_per2.print_info()
m_per3.print_info()
m_per4.print_info()

print(MyClass1.chack_age(m_per1.age))
print(MyClass1.chack_age(m_per2.age))
print(MyClass1.chack_age(m_per3.age))
print(MyClass1.chack_age(m_per4.age))


people = [m_per1, m_per2, m_per3, m_per4]
MyClass2.counter_ages(people)
