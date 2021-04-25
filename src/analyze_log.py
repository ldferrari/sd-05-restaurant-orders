import csv


def read_file(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    try:
        with open(path_to_file, encoding='utf-8') as file:
            return list(csv.reader(file))
    except FileExistsError:
        return 'File not found'


def most_requested(orders_list, client):
    orders_dict = {}
    for name, order, day in orders_list:
        if name == client:
            if order in orders_dict:
                orders_dict[order] += 1
            else:
                orders_dict[order] = 1
    return max(orders_dict, key=orders_dict.get)


def orders_counter(orders_list, client, meal):
    counter_food = 0
    for name, food, day in orders_list:
        if name == client and food == meal:
            counter_food += 1
    return counter_food


def never_did_it(orders_list, client, option):
    never_did = set()
    did_it = set()
    for order in orders_list:
        never_did.add(order[option])
        if order[0] == client:
            did_it.add(order[option])
    client_never_did = never_did.difference(did_it)
    return client_never_did


def analyze_log(path_to_file):
    orders = read_file(path_to_file)
    maria_favorite = most_requested(orders, 'maria')
    hamburguers_of_arnaldo = orders_counter(orders, 'arnaldo', 'hamburguer')
    joao_never_asked = never_did_it(orders, 'joao', 1)
    joao_never_visited = never_did_it(orders, 'joao', 2)

    with open("data/mkt_campaign.txt", "w") as log:
        log.write(f"{maria_favorite}\n")
        log.write(f"{hamburguers_of_arnaldo}\n")
        log.write(f"{joao_never_asked}\n")
        log.write(f"{joao_never_visited}\n")
