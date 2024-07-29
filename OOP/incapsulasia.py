
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



