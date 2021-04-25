import csv


def most_ordered_dish(logs, client):
    '''Retorna qual o prato mais pedido de um cliente.'''

    most_ordered = {}

    for log in logs:
        if log[0] == client and log[1] not in most_ordered:
            most_ordered[log[1]] = 1

        elif log[0] == client:
            most_ordered[log[1]] += 1

    # https://stackoverflow.com/a/280156
    return max(most_ordered, key=most_ordered.get)


def count_repeated_dish(logs, client, dish):
    '''Retorna quantas vezes um cliente pediu um prato.'''

    times_ordered = 0

    for log in logs:
        if log[0] == client and log[1] == dish:
            times_ordered += 1

    return times_ordered


def never_ordered_by_client(logs, client):
    '''Retorna os pratos nunca pedidos por um cliente.'''

    all_dishes = set()
    client_dishes = set()

    for log in logs:
        all_dishes.add(log[1])

        if log[0] == client:
            client_dishes.add(log[1])

    return all_dishes.difference(client_dishes)


def days_out(logs, client):
    '''Retorna os dias da semana em que o cliente nunca foi a lanchonete.'''

    restaurant_days = set()
    client_days = set()

    for log in logs:
        restaurant_days.add(log[2])

        if log[0] == client:
            client_days.add(log[2])

    return restaurant_days.difference(client_days)


def write_mkt_campaign(path, datas):
    '''Escreve dados em um arquivo txt.'''

    with open(path, 'w') as text_file:
        for data in datas:
            text_file.write("{0}\n".format(data))


def read_csv_data(path_to_file):
    '''Lê um arquivo csv e retorna uma lista das linhas.'''

    with open(path_to_file) as file:
        csv_reader = csv.reader(file)

        csv_content = list(csv_reader)

        return csv_content


def analyze_log(path_to_file):
    data_to_write = []
    campaign_file = 'data/mkt_campaign.txt'

    orders = read_csv_data(path_to_file)

    data_to_write.append(most_ordered_dish(orders, 'maria'))
    data_to_write.append(count_repeated_dish(orders, 'arnaldo', 'hamburguer'))
    data_to_write.append(never_ordered_by_client(orders, 'joao'))
    data_to_write.append(days_out(orders, 'joao'))

    write_mkt_campaign(campaign_file, data_to_write)
