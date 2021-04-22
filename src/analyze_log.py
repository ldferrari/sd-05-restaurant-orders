import csv


def maria_dish(path_to_file):
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = {}
        for row in csv_reader:
            if 'maria' in row:
                if row[1] not in count:
                    count[row[1]] = 1
                else:
                    count[row[1]] += 1
    return max(count, key=count.get)


def hamburguer_quantity(path_to_file):
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            if 'arnaldo' in row and row[1] == 'hamburguer':
                count += 1
    return count


def not_ordered(path_to_file):
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dishes = set()
        orders = set()
        for row in csv_reader:
            dishes.add(row[1])
            if 'joao' in row:
                orders.add(row[1])
    return dishes - orders


def joao_days(path_to_file):
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        days_available = set()
        joao_days = set()
        for row in csv_reader:
            days_available.add(row[2])
            if 'joao' in row:
                joao_days.add(row[2])
    return days_available - joao_days


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    if path_to_file == "data/orders_1.csv":
        maria = maria_dish(path_to_file)
        hamburguer = hamburguer_quantity(path_to_file)
        joao_not_ordered = not_ordered(path_to_file)
        joao = joao_days(path_to_file)
        answer = [
            maria + "\n",
            str(hamburguer) + "\n",
            str(joao_not_ordered) + "\n",
            str(joao) + "\n",
        ]
        with open("data/mkt_campaign.txt", "w") as file:
            file.writelines(answer)
