def main():
    n = int(input("Введіть число N: "))
    for i in range(n, 0, -1):
        num = n - i + 1
        for j in range(1, n + 1):
            if j <= n - i:
                print(" ", end=" ")
            else:
                print(num, end=" ")
                num += 1
        print("")


if __name__ == "__main__":
    main()

