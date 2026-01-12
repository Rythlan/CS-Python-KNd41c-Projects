def main():
    rows, cols = 7, 7
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            if j % 2 == 0:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)

    print("Результат генерації масиву 7x7:")
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
