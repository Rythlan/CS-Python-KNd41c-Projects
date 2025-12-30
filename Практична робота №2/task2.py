from math import sqrt
from lib.prime import is_prime


def calculate(m: int) -> float:
    return 1 / (sqrt(m) + sqrt(2))


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
