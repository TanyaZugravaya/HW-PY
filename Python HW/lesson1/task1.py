#Найдите сумму цифр трехзначного числа. 

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

num1 = int (input("Введите трехзначное число:  "))

a = num1 // 100
b = num1 // 10 % 10
c = num1 % 10

print (a + b + c)