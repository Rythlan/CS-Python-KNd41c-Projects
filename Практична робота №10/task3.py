import matplotlib.pyplot as plt
import json

with open('../Практична робота №9/teams.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

labels = [team['Name'] for team in data]
values = [team['Points'] for team in data]

plt.figure(figsize=(10, 8))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Розподіл очок команд')
plt.show()