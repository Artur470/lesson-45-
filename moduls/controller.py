from moduls import models

def controller_save_data(file_name, data):
    models.save_data(file_name, data)
def controller_remove_data(file_name, data):
    models.remove_file(file_name, data)
def controller_append_data(file_name, data):
    models.append_data(file_name, data)
def controller_coshuu(a, b):
    models.koshuu_funcsia(a,b)