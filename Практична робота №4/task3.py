def main():
    raw_input = input("Введіть елементи списку через пробіл: ")
    lst = raw_input.split()

    if lst:
        elements_to_add = lst[1::2]
        lst.extend(elements_to_add)
        print(f"Оновлений список: {lst}")
    else:
        print("Список порожній.")


if __name__ == "__main__":
    main()
