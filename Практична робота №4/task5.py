def main():
    m = int(input("Введіть кількість магазинів: "))
    common_products = set()

    for i in range(m):
        products_input = input(f"Введіть товари магазину №{i + 1} через пробіл: ")
        shop_products = set(products_input.split())

        if i == 0:
            common_products = shop_products
        else:
            common_products.intersection_update(shop_products)

    if common_products:
        print(f"Товари, наявні в усіх магазинах: {common_products}")
    else:
        print("Спільних товарів не знайдено.")


if __name__ == "__main__":
    main()
