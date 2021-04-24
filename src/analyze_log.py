import csv
from os.path import isfile

from collections import Counter


def count_client_order(orders):
    return dict(Counter([item for _, item, _ in orders]))


def filter_order(client, orders):
    return [order for order in orders if order[0] == client]


def analyze_log(path_to_file):
    try:
        isfile(path_to_file)
    except FileNotFoundError:
        raise FileNotFoundError("No such file or directory: ", path_to_file)
    else:
        with open(path_to_file, "r") as file:
            reader = csv.reader(file, delimiter=',')
            content = list(reader)
        menu = {item for _, item, _ in content}
        WEEK_DAYS = {day for _, _, day in content}
        maria = filter_order('maria', content)
        maria = count_client_order(maria)
        maria = max(maria, key=maria.get)
        arnaldo = filter_order('arnaldo', content)
        arnaldo = str(count_client_order(arnaldo)['hamburguer'])
        joao_orders = filter_order('joao', content)
        joao = {item for _, item, _ in joao_orders}
        joao = str(menu - joao)
        joao_days = {day for _, _, day in joao_orders}
        joao_days = str(WEEK_DAYS - joao_days)
        with open('./data/mkt_campaign.txt', 'w') as file:
            file.write(maria)
            file.write('\n')
            file.write(arnaldo)
            file.write('\n')
            file.write(joao)
            file.write('\n')
            file.write(joao_days)
            file.write('\n')


if __name__ == '__main__':
    analyze_log('./data/orders_1.csv')
