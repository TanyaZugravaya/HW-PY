# Задача 18:  
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input("Введите количество элементов массива (натуральное число): "))
from random import randint
A =[randint(1,10)for i in range(n)]
print(A)

X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
min = abs(X - A[0])
index = 0
for i in range(1, n):
       count = abs(X - A[i])
       if count < min:
           min = count
           index = i
print(f'Число {A[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A[index])}')
    