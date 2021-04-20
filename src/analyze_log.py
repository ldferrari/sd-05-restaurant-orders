import csv
from collections import defaultdict
import os
import errno

# 1. Em cada function, transformar orders_1.csv em objeto relevante
# 2. Functions necessárias para depois achar os 4 elementos pedidos


def get_all_dishes(path_to_file):
    all_dishes = set()
    with open(path_to_file) as file:
        reader = csv.reader(file)
        for line in reader:
            all_dishes.add(line[1])
    return all_dishes


def get_all_days(path_to_file):
    all_days = set()
    with open(path_to_file) as file:
        reader = csv.reader(file)
        for line in reader:
            all_days.add(line[2])
    return all_days


def dishes_by_customer(path_to_file, customer):
    dishes_customer = set()
    with open(path_to_file) as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] == customer:
                dishes_customer.add(line[1])
    return dishes_customer


def days_by_customer(path_to_file, customer):
    days_customer = set()
    with open(path_to_file) as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] == customer:
                days_customer.add(line[2])
    return days_customer


def most_ordered_dishes(path_to_file, costumer):
    # cannot be with set because each element would be unique
    # https://www.geeksforgeeks.org/defaultdict-in-python/
    ordered_dishes = defaultdict(int)
    with open(path_to_file) as file:
        reader = csv.reader(file)

        for line in reader:
            if line[0] == costumer:
                ordered_dishes[line[1]] += 1
    # print(ordered_dishes)
    return dict(ordered_dishes)
    # formato retornado: {'hamburguer': 16, 'pizza': 8, 'coxinha': 8}


# 3. Functions para o detalhe dos 4 elementos pedidos
# 3.1 Prato mais pedido por cliente ('maria')
def most_ordered_dish_by_customer(path_to_file, customer):
    dish = list(most_ordered_dishes(path_to_file, customer).keys())[0]
    return dish
    # formato retornado: hamburger


# 3.2 Contar vezes que cliente ('arnaldo') pediu prato ('hamburguer')
def count_dish_customer(path_to_file, customer, dish):
    count_dish = most_ordered_dishes(path_to_file, customer)[dish]
    return count_dish


# 3.3 Pratos que cliente ('joao') nunca pediu
def get_never_ordered(path_to_file, customer):
    all = get_all_dishes(path_to_file)
    by_customer = dishes_by_customer(path_to_file, customer)
    return all.difference(by_customer)


# 3.4 Dias que cliente ('joao') nunca foi na lanchonete
def get_never_went(path_to_file, customer):
    all = get_all_days(path_to_file)
    by_customer = days_by_customer(path_to_file, customer)
    return all.difference(by_customer)


# 4. Mandar as respostas no arquivo data/mkt_campaign.txt
def analyze_log(path_to_file):
    if os.path.isfile(path_to_file) and path_to_file.endswith('.csv'):
        data_path = 'data/orders_1.csv'
        text = []
        text.append(most_ordered_dish_by_customer(data_path, 'maria'))
        text.append(count_dish_customer(data_path, 'arnaldo', 'hamburguer'))
        text.append(get_never_ordered(data_path, 'joao'))
        text.append(get_never_went(data_path, 'joao'))
        # print(final_text)
        destination_path = "data/mkt_campaign.txt"
        with open(destination_path, "w") as final_file:
            for element in text:
                final_file.write(str(element) + "\n")
                # https://stackoverflow.com/questions/37289951/how-to-write-to-a-csv-line-by-line
    else:
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), path_to_file
        )
    # https://docs.python.org/3/library/os.html
    # https://stackoverflow.com/questions/36077266/how-do-i-raise-a-filenotfounderror-properly


if __name__ == "__main__":
    print(analyze_log('data/orders_1.csv'))

# Honestidade acadêmica
# https://github.com/tryber/sd-05-restaurant-orders/pull/5/files
# https://github.com/tryber/sd-05-restaurant-orders/pull/3/files
