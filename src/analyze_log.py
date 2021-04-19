import csv
import errno
import os


def find_marias_top_dish(path_to_file):
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count_dishes = dict()

        for row in csv_reader:
            if 'maria' in row:
                count_dishes.setdefault(row[1], 0)
                count_dishes[row[1]] += 1
    return max(count_dishes, key=count_dishes.get)


def find_arnaldos_hamburguer_quantity(path_to_file):
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0

        for row in csv_reader:
            if 'arnaldo' in row and row[1] == 'hamburguer':
                count += 1

    return count


def find_joaos_zero_dishes(path_to_file):
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dishes_set = set()
        joao_orders = set()

        for row in csv_reader:
            dishes_set.add(row[1])
            if 'joao' in row:
                joao_orders.add(row[1])

    return dishes_set - joao_orders


def find_joaos_zero_days(path_to_file):
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        days_set = set()
        joao_days = set()

        for row in csv_reader:
            days_set.add(row[2])
            if 'joao' in row:
                joao_days.add(row[2])

    return days_set - joao_days


def analyze_log(path_to_file):
    filename = "data/mkt_campaign.txt"
    if os.path.isfile(filename):
        with open(filename, "+w") as campaing_file:
            campaing_file.write(
                find_marias_top_dish(path_to_file) + "\n"
            )
            campaing_file.write(
                str(find_arnaldos_hamburguer_quantity(path_to_file)) + "\n"
            )
            campaing_file.write(
                str(find_joaos_zero_dishes(path_to_file)) + "\n"
            )
            campaing_file.write(
                str(find_joaos_zero_days(path_to_file)) + "\n"
            )
    else:
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), filename
        )


# analyze_log("data/orders_1.csv")
