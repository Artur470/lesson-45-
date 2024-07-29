
##########  алгоритм  сортировка пузырьков ##############
"""
def bSort(array):
    length = len(array)#10
    for i in range(length):   # i = 1
        for j in range(0, length-i-1): # [1]
            if array[j] > array[j+1]:
                temp = array[j] #[3]
                array[j] = array[j+1]
                array[j+1] = temp

array = [3,4,6,7,5,3,2,4,6,8]# 3 4 6 5 3 2 4 6 7 8
bSort(array)                 # 3 4 5 6 3 2 4 6 7 8


"""

#      ##########алгоритм  сортировка  вставкой ###########
"""

def sel_sort(row):
    n = len(row)
    for i in range(n-1):
        m = i
        for j in range(i+1, n ):  #j 1
            if row[j] < row[m]: ###  6 < 2
                m = j
        temp =row[i]
        row[i] = row[m] # m 1
        row[m] = temp
    print(row)
row = [6,3,2,1,3,9,5] # 3 6 2 1 3 9 5
sel_sort(row)
print(row)

"""





#  колдонуучу x =  3 санын берсе экранга 3  чыксын эгерде бир дагы элемент жок болсо
             # табылган жок деп билдируу чыксын

"""

a = [2,3,4,6,4,3,2,57,3,2,43,67]
x = int(input("x :"))
test = 0
for i in range(len(a)):
    if a[i] == x:
        print(f" index бойунча  {i} сиз сураган сан {a[i]} ")
        test = 1
if test == 1:
    print("табылган жок")




"""


"""

#    пустой лист ачып ошонун ичине 15 chon , 50 kichine сандарды кошобуз
a = [1, 20, 30, 12, 56, 67,23,12,78]
result = []
min_element = 15
max_element = 50
for i in a :
    if i  != 20 and i != 30 and i != 23 :
        result.append(i)

print(result)
"""