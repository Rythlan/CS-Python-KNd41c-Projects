def main():
    word = input("Введіть, будь ласка, слово: ")

    while not word:
        word = input("Рядок порожній, введіть слово ще раз: ")

    result = word[::-1]
    print(f"Результат запису літер у зворотному порядку: {result}")


if __name__ == "__main__":
    main()