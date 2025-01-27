

salary=float(input("Введите ежемесячную зарплату: "))
credit=float(input("Введите сумму месячного платежа по кредиту в банке : "))
communal_service=float(input("Введите задолженность за коммунальные услуги : "))
itog=salary-(credit+communal_service)
print("Классические метод вывода. Остаток: ", float(itog)) # классический
print(f"а-строка.Остаток: {itog}") # ф-строка
print("Функция формат.Остаток: {}".format(itog)) # .format()).