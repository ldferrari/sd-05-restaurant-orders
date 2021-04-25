import csv


def read_csv(filepath):
    try:
        with open(filepath, "r") as file:
            orders_reader = csv.reader(file, delimiter=",", quotechar='"')
            orders = list(orders_reader)
    except FileNotFoundError:
        raise (FileNotFoundError(f"No such file or directory: '{filepath}'"))
    else:
        return orders


def top_maria_order(orders):
    dict_maria = {}
    for order in orders:
        if order[0] == "maria" and order[1] not in dict_maria:
            dict_maria[order[1]] = 1
        elif order[0] == "maria":
            dict_maria[order[1]] += 1
    return max(dict_maria, key=dict_maria.get)


def burgers_count_arnaldo(orders):
    burger_count = 0
    for order in orders:
        if order[0] == "arnaldo" and order[1] == "hamburguer":
            burger_count += 1
    return burger_count


def joao_decline(orders):
    all_meals = set()
    joao_ordered = set()
    for order in orders:
        if order[0] == "joao":
            joao_ordered.add(order[1])
        all_meals.add(order[1])
    return all_meals.difference(joao_ordered)


def joao_missing_days(orders):
    all_days = set()
    days_with_joao = set()
    for order in orders:
        if order[0] == "joao":
            days_with_joao.add(order[2])
        all_days.add(order[2])
    return all_days.difference(days_with_joao)


def analyze_log(path_to_file):
    orders = read_csv(path_to_file)
    maria = top_maria_order(orders)
    arnaldo_count = burgers_count_arnaldo(orders)
    joao_declines = joao_decline(orders)
    joao_missing = joao_missing_days(orders)
    txt_text = [
        maria + "\n",
        str(arnaldo_count) + "\n",
        str(joao_declines) + "\n",
        str(joao_missing) + "\n",
    ]

    with open("data/mkt_campaign.txt", "w") as file:
        file.writelines(txt_text)
