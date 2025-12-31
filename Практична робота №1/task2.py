def main():
    stipend = 50.0
    expenses = 80.0
    total_debt = 0.0

    print("Розрахунок боргу за 10 місяців:")
    for month in range(1, 11):
        debt = expenses - stipend
        total_debt += debt
        print(f"{month} міс. | Витрати: {expenses:.2f} | Борг: {debt:.2f}")
        expenses *= 1.02

    print(f"Разом до виплати: {total_debt:.2f} грн")


if __name__ == "__main__":
    main()

