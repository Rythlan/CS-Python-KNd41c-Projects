# 2 * a/b + 1 if a > b
# -445 if a == b
# (b+5)/a if a < b


def equation(a: int, b: int) -> float:
    if a > b:
        return 2 * a / b + 1
    elif a == b:
        return -445
    else:
        return (b + 5) / a


def main():
    a = int(input("Введіть значення a: "))
    b = int(input("Введіть значення b: "))

    if (1 < a < 100) and (1 < b < 100):
        print(f"Відповідь: {equation(a, b):.2f}")
    else:
        print("Помилка: Числа a та b мають бути в діапазоні від 1 до 100.")


if __name__ == "__main__":
    main()
