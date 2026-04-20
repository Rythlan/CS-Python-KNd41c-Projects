import csv

print("--- Рівень інфляції у 2016 році ---")

col_name = 'Country Name'
col_year = '2016 [YR2016]'

def get_val(d):
    try: 
        return float(d[col_year])
    except (ValueError, TypeError, KeyError): 
        return None

try:
    filename = "./00bb4ee7-24dc-41b1-bf2a-f49a324ae042_Data.csv"
    
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        data_list = list(reader)
        
        for data in data_list:
            val = get_val(data)
            if val is not None:
                print(f"{data[col_name]}: {data[col_year]}%")
            
        print("-" * 30)
        
        try:
            user_input = input("Введіть поріг інфляції для пошуку: ")
            threshold = float(user_input)
        except ValueError:
            print("Помилка: Будь ласка, введіть числове значення.")
            exit() 

        with open("high_inflation.csv", "w", encoding="utf-8", newline='') as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(["Country Name", "Inflation"])

            found_count = 0
            for data in data_list:
                val = get_val(data)
                if val is not None and val > threshold:
                    writer.writerow([data[col_name], data[col_year]])
                    found_count += 1

        print(f"Пошук завершено. Знайдено країн: {found_count}. Результати збережено у high_inflation.csv")

except FileNotFoundError:
    print("Помилка: Файл не знайдено. Перевірте шлях до файлу.")
except Exception as e:
    print(f"Сталася непередбачувана помилка: {e}")
