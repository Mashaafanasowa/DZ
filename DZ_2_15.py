num=int(input("Введите четырехзначное число :"))
units=num%10
dozens=(num%100)//10
hundredths=((num//100)%10)
thousands=num//1000
sum=thousands+units+dozens+hundredths
Composition=thousands*units*dozens*hundredths
print(f"Сумму числе в четырехзначном числе:{sum}")
print(f"Произведение в четырехзначном числе:{Composition}")