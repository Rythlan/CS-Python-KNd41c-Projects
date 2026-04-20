import json
import os

def initialize_file():
    if os.path.exists("teams.json"):
        return 
    
    initial_teams = [
        {"Name": "Dynamo Kyiv", "Points": 25},
        {"Name": "Shakhtar Donetsk", "Points": 22},
        {"Name": "Dnipro-1", "Points": 19},
        {"Name": "Zorya Luhansk", "Points": 15},
        {"Name": "Polissya Zhytomyr", "Points": 18},
        {"Name": "Karpaty Lviv", "Points": 12},
        {"Name": "Vorskla Poltava", "Points": 14},
        {"Name": "Metalist Kharkiv", "Points": 10},
        {"Name": "Chornomorets Odesa", "Points": 8},
        {"Name": "Arsenal Kyiv", "Points": 5}
    ]
    with open("teams.json", "w", encoding="utf-8") as f:
        json.dump(initial_teams, f, indent=4, ensure_ascii=False)


def view_data():
    try:
        with open("teams.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            print("\n--- Список команд ---")
            for item in data:
                print(f"Команда: {item['Name']}, Очки: {item['Points']}")
    except Exception as e:
        print(f"Помилка при читанні: {e}")

def add_data():
    try:
        with open("teams.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        print("\n--- Додавання нової команди ---")
        new_name = input("Назва команди: ")
        new_points = int(input("Кількість очок: "))
        
        data.append({"Name": new_name, "Points": new_points})
        
        with open("teams.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("Запис успішно додано.")
    except Exception as e:
        print(f"Помилка: {e}")

def delete_data():
    try:
        with open("teams.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        target = input("\nВведіть назву команди для видалення: ")
        
        found = False
        for team in data:
            if team['Name'] == target:
                data.remove(team)
                found = True
                break
        
        if not found:
            print("Команду не знайдено.")
        else:
            with open("teams.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Команду '{target}' видалено.")
    except Exception as e:
        print(f"Помилка: {e}")

def search_data():
    try:
        with open("teams.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        target = input("\nВведіть назву команди для пошуку: ")
        results = [team for team in data if target.lower() in team['Name'].lower()]
        
        if results:
            print("Результати пошуку:")
            for r in results:
                print(f"- {r['Name']} ({r['Points']} очок)")
        else:
            print("Нічого не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

def solve_variant_task():
    try:
        with open("teams.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        sorted_teams = sorted(data, key=lambda x: x['Points'], reverse=True)
        
        if len(sorted_teams) < 3:
            print("Недостатньо даних для визначення призерів.")
            return

        champion = sorted_teams[0]
        second = sorted_teams[1]
        third = sorted_teams[2]

        print("\n--- РЕЗУЛЬТАТИ ЧЕМПІОНАТУ ---")
        print(f"а) Чемпіон: {champion['Name']}")
        print(f"б) Друге місце: {second['Name']}")
        print(f"   Третє місце: {third['Name']}")

        winners = {
            "Champion": champion,
            "Second_Place": second,
            "Third_Place": third
        }
        
        with open("winners.json", "w", encoding="utf-8") as f:
            json.dump(winners, f, indent=4, ensure_ascii=False)
        
        print("\nРезультати збережено у winners.json")

    except Exception as e:
        print(f"Помилка при вирішенні завдання: {e}")


def main():
    initialize_file()
    
    while True:
        print("\n=== МЕНЮ (Робота з JSON) ===")
        print("1 - Вивести вміст JSON")
        print("2 - Додати запис")
        print("3 - Видалити запис")
        print("4 - Пошук за назвою")
        print("5 - Визначити чемпіонів (Варіант)")
        print("6 - Вихід")
        
        choice = input("Оберіть варіант: ")

        if choice == '1':
            view_data()
        elif choice == '2':
            add_data()
        elif choice == '3':
            delete_data()
        elif choice == '4':
            search_data()
        elif choice == '5':
            solve_variant_task()
        elif choice == '6':
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()