def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a -= b  
        else:
            b -= a  
    return a if a != 0 else b  


a = int(input("Введите первое натуральное число: "))
b = int(input("Введите второе натуральное число: "))

if a <= 0 or b <= 0:
    print("Ошибка: оба числа должны быть натуральными.")
else:
    print(f"Наибольший общий делитель: {gcd(a, b)}")
