"""
1 нижние примеры с помошью функции

бир пустой лист жаратып анын ичине 60 чейинки сандарды кошкула
my_list = [1,2,3,5,7,8,6,5,4,3,6,978,5,43,,54,56]

"""

"""2 листтин ичиндеги элементтердин биринчи жана акыркы сандарын кошкула 

"""

"""3 my_info деген бир создук  (dic)   жарат name ачкычы  мааниси озунуздун атыныз болсун!

"""
"""4 a , b сандын кайсынысы чон кичине экенин тап 

"""
"""5 уч сан киргизип ошонун эн чон санын тап 

"""
"""
def sum(my_list):
    result = []
    for element in my_list:
        if element < 60:
            result.append(element)
    return result


my_list = [1,3,3,56,6,78,90,54,3,2,7,87,7]
result = sum(my_list)
print(result)
"""



"""
def suma(a):
    result = [0] + a[-1]
    return result


a = [4,3,6,8,9,0,6,4]
result = suma(a)
print(result)
"""
"""
def returnName(name):
    my_info = {"achkych": name, }
    return my_info

result = returnName("Artur")
print(result)

"""



"""
def numberMaxandMin():
    if a > b :
        print("a > b")
    elif a < b :
        print("a < b ")
    else:
        print("a == b")
a = int(input("a :"))
b = int(input("b :"))

numberMaxandMin()

"""
##############  рекурсия  ##############

"""
`
def f (n):
    if n == 0   :
        return 0
    return n * f(n -1)
print(f(10))


"""
