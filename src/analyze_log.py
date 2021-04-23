import csv


def csv_importer(filepath):
    try:
        with open(filepath, "r") as file:
            file_reader = csv.reader(file, delimiter=",", quotechar='"')
            fileList = list(file_reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: '{filepath}'")
    else:
        return fileList


def order_by_maria(data):
    maria_ordered = {}

    for order in data:
        if order[0] == "maria" and order[1] not in maria_ordered:
            maria_ordered[order[1]] = 1
        elif order[0] == "maria":
            maria_ordered[order[1]] += 1
    return max(maria_ordered, key=maria_ordered.get)


def arnaldos_burger(data):
    arnaldo_ordered = 0

    for order in data:
        if order[0] == "arnaldo" and order[1] == "hamburguer":
            arnaldo_ordered += 1
    return arnaldo_ordered


def joao_not_order(data):
    all_meals = set()
    order_by_joao = set()

    for order in data:
        if order[1] not in all_meals:
            all_meals.add(order[1])
        if order[0] == "joao" and order[1] not in order_by_joao:
            order_by_joao.add(order[1])
    return all_meals.difference(order_by_joao)


def days_joao_was_not(data):
    all_days = set()
    days_by_joao = set()

    for order in data:
        if order[2] not in all_days:
            all_days.add(order[2])
        if order[0] == "joao" and order[2] not in days_by_joao:
            days_by_joao.add(order[2])
    return all_days.difference(days_by_joao)


def analyze_log(path_to_file):
    data = csv_importer(path_to_file)
    # print('***data***', data)
    maria_order = order_by_maria(data)
    # print('***mariaOrder***', maria_order)
    arnaldos_hamburguer = arnaldos_burger(data)
    # print('***arnaldoburger***', arnaldos_hamburguer)
    joao_never_order = joao_not_order(data)
    # print('***joaoordernot***', joao_never_order)
    days_joao_not = days_joao_was_not(data)
    # print('***dayjoaonot***', days_joao_not)
    txt_text = [
        str(maria_order) + "\n",
        str(arnaldos_hamburguer) + "\n",
        str(joao_never_order) + "\n",
        str(days_joao_not) + "\n",
    ]

    with open("data/mkt_campaign.txt", "w") as file:
        file.writelines(txt_text)

# analyze_log("data/orders_1.csv")
