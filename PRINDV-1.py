
A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B (A < B): "))


if A >= B:
    print("Ошибка: A должно быть меньше B.")
else:
   
    for i in range(A, B + 1):
        for j in range(i - A + 1):  
            print(i, end=' ')
