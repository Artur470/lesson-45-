


"""канкулятор жазабыз

шарты:

колдунуучу а санын киргизет андан кийин
операцияны киргизет (+ - * / )
андан кийин b санын киргизет  кайсы оперцияны
киргизгенде ошого жараша жооп беруу керек
пример
>10
>  +
>4
#>>>>>14 жооп чыгыш керек
"""


"""


a = int(input("a sanyn kirgiz"))
o= input("o operazia kirgiz")
b = int(input("b sanyn kirgiz"))

if  o == "*":
    print(a * b)

elif o == "+":
    print(a + b)

elif o == "/":
    print(a / b)

else:
    print("tuura amaldy atkarynyz!")

"""
"""

     # string
s = 'balykchy'
print(s[-5])


"""


"""1 колдонуучу n санын киргизген 0  n < = 12  n саны  n ге int(input koldon
кайсы ай экенин корсотот эгреде 5 деген сан берсе Май
пример 
>5
>>>>май

"""
"""

n = int(input(" N : "))
if 0 < n and n <= 12 :
    if n == 1 :
        print("январь")
    elif n == 2 :
        print("февраль")
    else:
        print("мындай ай базада жок")
else:
    print(" туура аткарыныз!")


"""

"""2 колдонуучу n санын киргизгенде  0 < n < = 12 n саны 
кайсы мезгил 12 кыш  деп чыксын! анткени 12 ай бул кыш мезгилинде 
жайгашкан
"""





"""
n = int(input(" N : "))
if 0 < n or  n <= 12 :
    if n >= 12 and  n <= 2 :
         print("кыш")
    elif n >= 3 and n <= 5 :
        print("жаз")
    elif n >= 6 and n <= 8 :
        print("жай")
    else:
        print("куз")

"""

#
#
# a = int(input("введите число:"))
# if a < 0:
#    print("Neg")
# elif a == 0:
#    print("Zero")
# else:
#    print("Pos")


# b = (1,32,3,5,2,3,4,5,6,4,2,2,12,1)
#
# #print(len(set(b)))
# count = 0
# for item in set(b):
#     count = count + 1
# print(count)



# списокb = (1,32,3,5,2,3,4,5,6,4,2,2,12,1)


#
#
# # создается пустой список уникальных элементов
# unique_elements = set()
#
# # проходит по каждому списка b
# index = 0
# while index < len(b):
#     unique_elements.add(b[index])
#     index += 1
#
# # выводим количество уникальных элементов
# print("количество уникальных элементов списка ", len(unique_elements))
#
#

"""

def find_most_frequent(a, b, c):
   
    if a > b and a > c:
        return a  
    elif b > a and  b > c  :
        return b 
    else:
        print(c)


a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))



result = find_most_frequent(a,b,c)
print(result)

"""

"""

a = int(input("a :"))
b = int(input("b :"))

for i in range(a , b+1, 1 ):
    print(i)


"""




""" тапшырма: int(input) колдонуп  a ,b санын берип  цикл менен 
кылабыз  пример a 10 b 20 берсе 10 ,11,12,13,14,15,16,17,18,19,20

 2 : a саны b санынан кичине болушу шарт 
  эгерде андай болбосо экранга a саны b санынан кичине болушу
  шарт деген билдируу чыксын!!!
 
 3 : эгерде колдонуучу  сандын ордуна тамга берсе try exept менен ошибканы 
    кармап тамга эмес сан  киргиз деп чыксын!!!
 
"""

"""
try:
    a = int(input("a :"))
    b = int(input("b :"))
    if a < b:
        for i in range(a , b+1, 1 ):
            print(i)
    else:
        print(" a саны b санынан кичине болушу шарт !!")
except:
    print(" тамга эмес сан киргиз!")



"""





####################### Файлдар менен иштоо #################################

""" with open (" бул жерге файлдын аты   "  "  бул жерге режим корсотулот ) as file :
    open бул файлдар менен иштоо даяр функция
    my_file обектиге берилген ат 
    режимдин 3 туру бар 
    1  " w ", бул соз (write) жазуу учун ачканда колдонобуз
    2  " r " бул соз (read) окуу учун колдонобуз 
    3  " a " бул соз (append) маалыматты  кошуу учун колдонобуз 
    
    
"""
#
# def work_with_file(name, rejim):
#     with open(name, 'w') as file:
#         file.write(rejim)
#
#
# work_with_file("index.txt", "salamBektur")



