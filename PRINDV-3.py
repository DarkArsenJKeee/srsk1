import math

def left_side(x):
    return (1 + 2 * x**2) * math.exp(x**2)

def right_side(x, epsilon):
    total = 1 
    n = 1
    term = 1  

  
    while True:
        term = (2 * n + 1) * (x**(2 * n)) / math.factorial(n)
        total += term
        
        if abs(left_side(x) - total) < epsilon:  
            break
        n += 1

    return n, total

def main():
    x = float(input("Введите значение x: "))
    epsilon = float(input("Введите допустимую погрешность ε: "))

    num_terms, total = right_side(x, epsilon)
    left = left_side(x)

    print(f"Левая часть: {left}")
    print(f"Правая часть (разложение): {total}")
    print(f"Количество членов ряда: {num_terms}")
    print(f"Погрешность: {abs(left - total)}")

if __name__ == "__main__":
    main()
