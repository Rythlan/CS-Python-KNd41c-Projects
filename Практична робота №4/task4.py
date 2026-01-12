def main():
    raw_input = input("Введіть елементи списку через пробіл: ")
    lst = raw_input.split()

    target = input("Введіть елемент, для якого потрібно знайти сусідів: ")

    if target in lst:
        idx = lst.index(target)
        if 0 < idx < len(lst) - 1:
            print(f"Сусідні елементи: {lst[idx - 1]} та {lst[idx + 1]}")
        elif idx == 0:
            print("Це перший елемент, у нього є тільки правий сусід.")
        else:
            print("Це останній елемент, у нього є тільки лівий сусід.")
    else:
        print("Зазначеного елемента немає у списку.")


if __name__ == "__main__":
    main()
