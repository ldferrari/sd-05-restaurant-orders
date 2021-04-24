import csv


def maria(data):
    maria_orders = dict()
    for order in data:
        if 'maria' in order:
            maria_orders.setdefault(order[1], 0)
            maria_orders[order[1]] + 1
    return max(maria_orders, key=maria_orders.get) + '\n'


def joao(data):
    days = set()
    catalogue = set()
    joao_days = set()
    joao_orders = set()
    for order in data:
        catalogue.add(order[1])
        days.add(order[2])
        if 'joao' in order:
            joao_orders.add(order[1])
            joao_days.add(order[2])
    return [str(catalogue - joao_orders) + "\n", str(days - joao_days) + "\n"]


def arnaldo(data):
    arnaldo_counter = 0
    for order in data:
        if 'arnaldo' in order and order[1] == 'hamburguer':
            arnaldo_counter += 1
    return str(arnaldo_counter) + '\n'


def analyze_log(path_to_file):
    data = []
    if not path_to_file.split(".")[1] == "csv":
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    with open(path_to_file) as file_input:
        data.extend(csv.reader(file_input, delimiter=","))
    out = [maria(data), arnaldo(data), *joao(data)]
    with open("data/mkt_campaign.txt", "w") as file_output:
        file_output.writelines(out)
