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


def never_asked_meals(orders_list, client):
    never_asked = set()
    did_asked = set()
    for name, food, day in orders_list:
        if food not in did_asked:
            never_asked.add(food)
        if name == client:
            if food in never_asked:
                never_asked.remove(food)
            did_asked.add(food)
    return never_asked


def days_never_went(orders_list, client):
    never_went = set()
    did_went = set()
    for name, food, day in orders_list:
        if day not in did_went:
            never_went.add(day)
        if name == client:
            if day in never_went:
                never_went.remove(day)
            did_went.add(day)
    return never_went


def analyze_log(path_to_file):
    orders = read_file(path_to_file)
    maria_favorite = most_requested(orders, 'maria')
    hamburguers_of_arnaldo = orders_counter(orders, 'arnaldo', 'hamburguer')
    joao_never_asked = never_asked_meals(orders, 'joao')
    joao_never_went = days_never_went(orders, 'joao')

    with open("data/mkt_campaign.txt", "w") as log:
        log.write(f"{maria_favorite}\n")
        log.write(f"{hamburguers_of_arnaldo}\n")
        log.write(f"{joao_never_asked}\n")
        log.write(f"{joao_never_went}\n")
