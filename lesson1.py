#                                              30.11.2024

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет, Я из города {self.city}")

    def is_adult(self):
        return self.age >= 18


    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Город: {self.city}"



person1 = Person("Kerimkazy", 25, "Bishkek")
person2 = Person("Kairat", 16, "Bishkek")
person3 = Person("Amir", 19, "Bishkek")

person1.introduce()
person2.introduce()
person3.introduce()

print(person1)
print(person2)
print(person3)
