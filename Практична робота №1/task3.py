def main():
    n = int(input("Введіть число N: "))
    for i in range(1, n + 1):
        num = n
        for j in range(1, n + 1):
            if j < i:
                print(" ", end=" ")
            else:
                print(num, end=" ")
                num -= 1
        print("")


if __name__ == "__main__":
    main()
