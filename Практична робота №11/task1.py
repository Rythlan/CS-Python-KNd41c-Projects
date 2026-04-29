import pandas as pd

data = {
    "Команда":["Dynamo", "Shakhtar", "Zorya", "Vorskla", "Desna", "Oleksandriya", "Kolos"],
    "Очки":[45, 42, 38, 35, 31, 29, 25],
    "Регіон":["Центр", "Схід", "Схід", "Центр", "Північ", "Центр", "Центр"],
    "Бюджет":[30, 40, 10, 8, 5, 6, 4],
    "Гравці":[25, 26, 24, 23, 22, 24, 25]
}

df = pd.DataFrame(data)
df["Ціна_гравця"] = df["Бюджет"] / df["Гравці"]

print("--- Базовий аналіз ---")
print(df.head(3))
print("Типи даних:\n", df.dtypes)
print("Розмір датафрейму:", df.shape)
print(df.describe())

print("\n--- Фільтрація (>30 очок) та сортування ---")
print(df[df["Очки"] > 30])
print(df.sort_values(by="Очки", ascending=False).head(3))

print("\n--- Групування та агрегація ---")
print(df.groupby("Регіон")[["Очки", "Бюджет"]].mean())
print("Максимальний бюджет по регіонах:\n", df.groupby("Регіон")["Бюджет"].max())
print("Кількість унікальних команд:", df["Команда"].nunique())