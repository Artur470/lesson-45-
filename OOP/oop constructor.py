############### incapsulaisa #################
class Car:
    def __init__(self, model, marka, color):
        self.__model = model
        self.__marka = marka
        self.__color = color

    def get_color(self):
        return self.__color
    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        self.__model = new_model

    def start(self):
        print(f"{self.__model} - {self.__marka} is starting!!!")
    def move(self):
        print(f"{self.__model} - {self.__marka}is moving!!!")
    def stop(self):
        print(f" {self.__model} - {self.__marka}is stoping!!!")

    def distplay_info(self):
        print(f" model : {self.__model}\n"
              f" marka : {self.__marka}\n"
              f" color : {self.__color}\n"
              )
#
#
# mers = Car("Mers", "124", "write")
# print(mers.get_color())
# print(mers.get_model())
# mers.set_model("Mazda")
# mers.model = "BMW"
# mers.marka = "f90"
# mers.color = "black"
# mers.distplay_info()

"""





""""""

class Calculator:
    def __init__(self, number1, operration ,number2 ):
        self.__a = number1
        self.__operation = operration
        self.__b = number2
    def get_a(self):
        return self.__a
    def get_operation(self):
        return self.__operation
    def get_b(self):
        return self.__b
    def set_a(self, new_a):
        self.__a = new_a
    def set_operation(self, new_operation):
        self.__operation = new_operation
    def set_b(self, new_b):
        self.__b = new_b
    def plus(self):
        result = self.get_a() + self.get_b()
        print(f"koshuldu : {result}")
    def minus(self):
        result = self.get_a() - self.get_b()
        print(f"minus boldu : {result}")
    def umnoj(self):
        result = self.get_a() * self.get_b()
        print(f" umnojenie atkaryldy : {result}")
    def boluu(self):
        result = self.get_a() / self.get_b()
        print(f" bolundu : {result}")

    def oper(self):
        if self.get_operation() == "+":
            self.plus()
        elif self.get_operation() == "-":
            self.minus()
        elif self.get_operation() == "/":
            self.boluu()
        elif self.get_operation() == "*":
            self.umnoj()
        else:
            print("амалды туура аткарыныз!")
calculator = Calculator(10, "+", 200)
calculator.oper()


"""

"""



class Car:
    def __init__(self, model, marka, color):
        self.__model = model
        self.__marka = marka
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        self.__color = new_color

    def start(self):
        print(f"{self.__model} - {self.__marka} is starting!!!")
    def move(self):
        print(f"{self.__model} - {self.__marka}is moving!!!")
    def stop(self):
        print(f" {self.__model} - {self.__marka}is stoping!!!")

    def distplay_info(self):
        print(f" model : {self.__model}\n"
              f" marka : {self.__marka}\n"
              f" color : {self.__color}\n"
              )

mers = Car("Mers", "124", "write")
print(mers.get_color())
mers.set_color("yellow")

mers.start()
mers.distplay_info()


"""
