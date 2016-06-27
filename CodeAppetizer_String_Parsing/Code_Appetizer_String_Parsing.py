

def menu_prices(menu_list):
    item_prices = {}
    for food in menu_list:
        detail_list = food.split(",")
        item_name = detail_list[0].split(":")[1]
        item_price = float(detail_list[1].split(":")[1])
        item_prices[item_name] = item_price

    return item_prices


def main():
    menu_list = ["food:hotdog,price:5.50","food:burger,price:9.50",
        "food:fries,price:4.00","food:shake, price:5.00"]

    print menu_prices(menu_list)


if __name__ == "__main__":
    main()
    