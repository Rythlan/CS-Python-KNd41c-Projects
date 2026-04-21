football_teams = {
    "Dynamo": 45,
    "Shakhtar": 42,
    "Zorya": 38,
    "Vorskla": 35,
    "Desna": 31,
    "Oleksandriya": 29,
    "Kolos": 25,
    "Dnipro-1": 22,
    "Mariupol": 18,
    "Rukh": 15,
}


def print_teams(teams):
    print("\n--- Список команд ---")
    for team, score in teams.items():
        print(f"Команда: {team} - Очки: {score}")


def add_team(teams):
    name = input("Введіть назву нової команди: ")
    try:
        score = int(input("Введіть кількість очок: "))
        teams[name] = score
        print(f"Команду {name} додано!")
    except ValueError:
        print("Помилка: Кількість очок має бути цілим числом!")


def del_team(teams):
    name = input("Введіть назву команди для видалення: ")
    try:
        del teams[name]
        print(f"Команду {name} видалено.")
    except KeyError:
        print("Помилка: Такої команди не існує в словнику!")


def print_sorted_by_name(teams):
    print("\n--- Відсортовано за алфавітом ---")
    sorted_teams = {k: teams[k] for k in sorted(teams)}
    for team, score in sorted_teams.items():
        print(f"Команда: {team} - Очки: {score}")


def find_winners(teams: dict[str, int]):
    print("\n--- Переможці турніру ---")
    if len(teams) < 3:
        print("Недостатньо команд для визначення топ-3 місць.")
        return

    sorted_teams = sorted(
        teams.items(), key=lambda item: item[1], reverse=True
    )

    print(f"🥇 Чемпіон: {sorted_teams[0][0]} (Очки: {sorted_teams[0][1]})")
    print(f"🥈 2 місце: {sorted_teams[1][0]} (Очки: {sorted_teams[1][1]})")
    print(f"🥉 3 місце: {sorted_teams[2][0]} (Очки: {sorted_teams[2][1]})")


while True:
    print("\n" + "=" * 40)
    print("1 - Вивести всі команди")
    print("2 - Додати команду")
    print("3 - Видалити команду")
    print("4 - Вивести словник, відсортований за назвами")
    print("5 - Визначити чемпіона та 2-3 місця (Варіант 17)")
    print("0 - Вийти")
    print("=" * 40)

    choice = input("Введіть пункт меню: ")

    if choice == "1":
        print_teams(football_teams)
    elif choice == "2":
        add_team(football_teams)
    elif choice == "3":
        del_team(football_teams)
    elif choice == "4":
        print_sorted_by_name(football_teams)
    elif choice == "5":
        find_winners(football_teams)
    elif choice == "0":
        print("Вихід з програми. До побачення!")
        break
    else:
        print("Невірний ввід, спробуйте ще раз.")
