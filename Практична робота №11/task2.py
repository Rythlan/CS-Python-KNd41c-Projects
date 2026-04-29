import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = pd.read_csv('./comptagevelo2014.csv', parse_dates=['Date'], index_col='Date')

print(df.head(2))
print(df.info())
print(df.describe())

print("\nЗагальна кількість на всіх доріжках:", df.sum(numeric_only=True).sum())
print("\nКількість по кожній доріжці:\n", df.sum(numeric_only=True))

df_monthly = df.resample('ME').sum(numeric_only=True)
paths =['Rachel / Papineau', 'Berri1', 'Maisonneuve_1']

print("\nНайпопулярніший місяць:")
for p in paths:
    if p in df_monthly.columns:
        print(f"{p}: {df_monthly[p].idxmax().month}")

if 'Berri1' in df_monthly.columns:
    df_monthly['Berri1'].plot(kind='bar', color='teal', figsize=(10, 5))
    plt.title('Berri1 (2014)')
    plt.tight_layout()
    plt.savefig('task2_plot.png')
    plt.show()