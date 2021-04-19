import csv
# https://docs.python.org/3.8/library/functions.html#max
# https://docs.python.org/3.8/library/stdtypes.html#set


def parse_content(path_to_file):
    restaurant_data = []

    with open(path_to_file, 'r') as file:
        reader = csv.DictReader(
            file, fieldnames=['name', 'food', 'date']
        )

        for row in reader:
            restaurant_data.append(row)

    return restaurant_data


def customer_favorites(name, restaurant_data):
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


def marketing_content(content, path_to_file):
    with open(path_to_file, "w") as file:
        file.write(content)


def analyze_log(path_to_file):
    restaurant_data = parse_content(path_to_file)

    content = (
        f"{customer_favorites('maria', restaurant_data)}\n"
        f"{customer_order_count('arnaldo', 'hamburguer', restaurant_data)}\n"
        f"{unpopular_dishes('joao', 'food', restaurant_data)}\n"
        f"{unpopular_dishes('joao', 'date', restaurant_data)}"
    )

    marketing_content(content, './data/mkt_campaign.txt')
