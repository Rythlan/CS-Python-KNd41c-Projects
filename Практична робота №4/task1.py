def main():
    n = int(input("n = "))
    print(f"Введіть {n} елементів масиву через пробіл:")
    arr = list(map(float, input().split()))

    odd_elements = [x for x in arr if x % 2 != 0]

    if odd_elements:
        avg = sum(odd_elements) / len(odd_elements)
        print(f"Середнє арифметичне непарних елементів: {avg:.2f}")
    else:
        print("Непарних елементів не знайдено.")

    negative_reversed = [x for x in arr if x < 0][::-1]
    print(f"Від’ємні елементи у зворотному порядку: {negative_reversed}")


if __name__ == "__main__":
    main()
