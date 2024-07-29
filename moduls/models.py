from moduls import models
import os
def save_data(file_name, data):
    with open (file_name,"w")as file:
        file.write(data)

def append_data(file_name, data):
    with open(file_name, "a")as file:
        file.write(data)


def read_data(file_name):
    with open(file_name, "r")as file :
        result = file.read()
        return result

def remove_file(file_name, data):
    try:
        os.remove(file_name, data)
        return ("успешно удалено !")
    except:
        return ("ошибка ")


def koshuu_funcsia(a ,b ):
    result = a +b
    print(result)