num=int(input("Введите трехзначное число:"))
units=num%10
dozens=(num%100)//10
hundredths=num//100
sum=units+dozens+hundredths
Composition=units*dozens*hundredths
print(f"Число единиц в трехзначном числе:{units}")
print(f"Число десятков в трехзначном числе:{dozens}")
print(f"Сумму числе в трехзначном числе:{sum}")
print(f"Произведение в трехзначном числе:{Composition}")