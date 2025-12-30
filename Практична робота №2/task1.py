from math import sqrt, isqrt


def calculate(m: int) -> float:
    return 1 / (sqrt(m) + sqrt(2))


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False

    return True


def main():
    m = int(input("Введіть число m: "))

    print(f"Відповідь z: {calculate(m):.3f}")

    n = int(input("Введіть число n: "))

    if is_prime(n):
        print(f"Число N: {n} просте число.")
    else:
        print(f"Число N: {n} непросте число.")


if __name__ == "__main__":
    main()
