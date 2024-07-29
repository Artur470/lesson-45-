
"""

class Animal:
    def __init__(self, color, weight, food ):
        self.color = color
        self.weight = weight
        self.food = food

    def move(self):
        print(f"{self.name} is moving!")

    def age(self):
        print("Animal is eating!")

    def drink(self):
        print(f"   {self.name} is drinking!")

class Dog(Animal):
    def __init__(self, color, weight, food, name, age):
        super().__init__(color, weight, food)
        self. name = name
        self.age = age


    def voice(self):
        print("Gaf-Gaf")


tuzik = Dog("Black", 20, "Meat", "Tuzik", 2)
tuzik.move()
tuzik.voice()
tuzik.drink()



class Cat(Animal):
    def __init__(self, color, weight, food, name , age):
        super().__init__(color, weight, food)

        self.name = name
        self.age = age

    def voice(self):
        print("Miyau-Miyau")

    def darak(self):
        print(f"{self.name}  daraka chyk")


murka = Cat("write", 2, "milk", "Murka", 1)
murka.move()
murka.voice()

"""

