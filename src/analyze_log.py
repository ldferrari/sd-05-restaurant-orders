import csv


def shred_file(path_to_file):
    restaurant_data = []

    with open(path_to_file, 'r') as file:
        reader = csv.DictReader(
            file, fieldnames=['name', 'food', 'date']
        )

        for row in reader:
            restaurant_data.append(row)

    return restaurant_data


def favorite_dishes(name, restaurant_data):
    menu_orders = [
        data['food']
        for data in restaurant_data
        if data['name'] == name
    ]

    favorites = max(menu_orders, key=menu_orders.count)

    return favorites


def customer_order_count(name, food, restaurant_data):
    menu_orders = [
        data['food'] for data in restaurant_data
        if data['name'] == name
        and data['food'] == food
    ]

    return len(menu_orders)


def unpopular_dishes(name, tab, restaurant_data):
    menu = set([data[tab] for data in restaurant_data])

    popular = set([
        data[tab]
        for data in restaurant_data
        if data['name'] == name
    ])

    unpopular = menu.difference(popular)

    return unpopular


def marketing_data(content, path_to_file):
    with open(path_to_file, "w") as file:
        file.write(content)


def analyze_log(path_to_file):

    restaurant_data = shred_file(path_to_file)

    content = (
        f"{favorite_dishes('maria', restaurant_data)}\n"
        f"{customer_order_count('arnaldo', 'hamburguer', restaurant_data)}\n"
        f"{unpopular_dishes('joao', 'food', restaurant_data)}\n"
        f"{unpopular_dishes('joao', 'date', restaurant_data)}"
    )

    marketing_data(content, './data/mkt_campaign.txt')
