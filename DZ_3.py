#Домашнее задание. Задание 3.

d_1=float(input("Введите диагональ 1: "))
d_2=float(input("Введите диагональ 2: "))
sum=(d_1*d_2)/2
print("Классический вывод.Площадь ромба: ", float(sum)) # классический
print(f"а-строка.Площадь ромба: {sum}") # ф-строка
print("Функция формат.Площадь ромба: {}".format(sum)) # .format()).