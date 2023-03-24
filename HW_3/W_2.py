# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5 
# 1 2 3 4 5 
# 6 
# -> 5

N = int(input("Введите количество чисел в массиве: "))
x = int(input("Введите искомое число: "))

from random import randint
list= []

for i in range(N):
    list.append(randint(1, N))
print(list)

if x in list:
    print(f"{x} - есть в списке")
else:
    result = abs(list[0] - x)
    res = list[0]
    for i in range(len(list)):
        if abs(list[i] - x) < result:
            result = abs(list[i] - x)
            res = list[i]
    print(f"{res} - самый близкий по величине элемент к {x}")