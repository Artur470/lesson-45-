
##################### ФУНКЦИЯ ############# def #######################


#
#
# n = int(input("ведите число!"))
# count = 0
#
# while ( n > 0 ):
#      count = count + 1
#      n = n // 10
# print("количество цифр равно ", count)

#
# def sandardy_koshuu(a , b ):
#      result = a + b
#      return result
#
# def countdigits():
#     n = int(input("ведите число "))
#
#     count = 0
#     while ( n > 0 ):
#         count = count + 1
#         n = n // 10
#     print("количество цифр равно ",count)
#
# print(sandardy_koshuu(2,5))
# print(sandardy_koshuu(2,5))
# print(sandardy_koshuu(2,5))
# print(sandardy_koshuu(2,5))
# print(sandardy_koshuu(2,5))
# print(sandardy_koshuu(2,5))
#


"""ТАПШЫРМА : def ФУНКЦИЯ КОЛДОНУП КАЛЬКУЛЯТОР ЖАЗАБЫЗ a operation b float(input) КОЛДОНОБУЗ
IF ELIF ELSE ШАРТ КОЙОБУЗ ОПЕРАЦИЯ АТКАРЫШ УЧУН
ПРИМЕР
a 5
oper +
b 5

#>>> 10
"""
#
# def plus(a,b):
#     print(a + b)
# def minus(a,b):
#     print(a - b)
# def umnaj(a,b):
#     print(a * b)
# def delen(a,b):
#     print(a / b)
#
#
# a = int(input(" a "))
# oper = input("oper")
# b = int(input(" b "))
#
#
# if oper == "+":
#     plus(a ,b)
# elif oper == "-":
#     minus(a ,b)
# elif oper == "*":
#     umnaj(a , b)
# elif oper == "/":
#     delen(a,b)
#
#
#
#
# def sum(*args):
#     result = 1
#     for  element in  args:
#         result = result * element
#     return result
# print(sum(3,2))
#

###### data structure #############

a  = [1,2,3,4,3,5,6,7,5] #LIST
s = {2,4,2,4,5,7,} #set
d = {2: 3,} #dictionry
t = (1,2
     ,3,4,
     5,5
     ) # kartesh

a = 1 #озгормо
b =[1,2,3,4,5,6,7] # data stucture


def say_hello(**kwargs):
    for value in kwargs.values():


        print(f"hello , {value}")

say_hello(name="Beka", surname="Babahanov")


