# Referências: https://www.kite.com/python/answers/
# how-to-find-the-max-value-in-a-dictionary-in-python
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


def most_ordered_by_maria(orders):
    ordered_by_maria = {}

    for order in orders:
        if order[0] == "maria" and order[1] not in ordered_by_maria:
            ordered_by_maria[order[1]] = 1
        elif order[0] == "maria":
            ordered_by_maria[order[1]] += 1

    return max(ordered_by_maria, key=ordered_by_maria.get)


def hamburguers_ordered_by_arnaldo(orders):
    hamburguer_counter = 0

    for order in orders:
        if order[0] == "arnaldo" and order[1] == "hamburguer":
            hamburguer_counter += 1

    return hamburguer_counter


def never_ordered_by_joao(orders):
    every_meal = set()
    ordered_by_joao = set()

    for order in orders:
        if order[0] == "joao":
            ordered_by_joao.add(order[1])
        every_meal.add(order[1])

    return every_meal.difference(ordered_by_joao)


def days_joao_did_not_show_up(orders):
    days = set()
    days_joao_showed_up = set()

    for order in orders:
        if order[0] == "joao":
            days_joao_showed_up.add(order[2])
        days.add(order[2])

    return days.difference(days_joao_showed_up)


def analyze_log(path_to_file):
    orders = read_csv(path_to_file)
    maria_order = most_ordered_by_maria(orders)
    arnaldo_hamburguer = hamburguers_ordered_by_arnaldo(orders)
    joao_never_ordered = never_ordered_by_joao(orders)
    joao_days = days_joao_did_not_show_up(orders)
    txt_text = [
        maria_order + "\n",
        str(arnaldo_hamburguer) + "\n",
        str(joao_never_ordered) + "\n",
        str(joao_days) + "\n",
    ]

    with open("data/mkt_campaign.txt", "w") as file:
        file.writelines(txt_text)


if __name__ == "__main__":
    # orders = read_csv("data/orders_1.csv")
    # print(most_ordered_by_maria(orders))
    # print(hamburguers_ordered_by_arnaldo(orders))
    # print(never_ordered_by_joao(orders))
    # print(days_joao_did_not_show_up(orders))
    analyze_log("data/orders_1.csv")
