import csv


def person_eats_dict(path_to_file, person):
    with open(path_to_file) as file:
        arquivo = csv.reader(file, delimiter=',')
        meals = {}
        for row in arquivo:
            if row[0] == person:
                if row[1] not in meals:
                    meals[row[1]] = 1
                else:
                    meals[row[1]] += 1
    return meals


def most_ordered(meals):
    # highest = sorted(meals.items(), key=lambda x: x[1], reverse=True)
    highest = sorted(meals, key=meals.get, reverse=True)
    return highest[0]
# maria = {'hamburguer': 16, 'pizza': 8, 'coxinha': 8}
# print(most_ordered(maria))


def how_many_times(item, meals):
    return meals[item]
# maria = {'hamburguer': 16, 'pizza': 8, 'coxinha': 8}
# print(how_many_times('pizza', maria))


def all_kinds_of_meals(path_to_file):
    with open(path_to_file) as file:
        arquivo = csv.reader(file, delimiter=',')
        all_meals = {}
        for row in arquivo:
            if row[1] not in all_meals:
                all_meals[row[1]] = 1
            else:
                all_meals[row[1]] += 1
    return all_meals
# print(all_kind_of_meals("data/orders_1.csv"))


def all_days(path_to_file):
    with open(path_to_file) as file:
        arquivo = csv.reader(file, delimiter=',')
        all_days = {}
        for row in arquivo:
            if row[2] not in all_days:
                all_days[row[2]] = 1
            else:
                all_days[row[2]] += 1
    return all_days
# print(all_days("data/orders_1.csv"))


def person_days_dict(path_to_file, person):
    with open(path_to_file) as file:
        arquivo = csv.reader(file, delimiter=',')
        days = {}
        for row in arquivo:
            if row[0] == person:
                if row[2] not in days:
                    days[row[2]] = 1
                else:
                    days[row[2]] += 1
    return days


def analyze_log(path_to_file):
    # raise NotImplementedError
    campaign = []

    maria_eats_all = person_eats_dict(path_to_file, 'maria')
    maria_eats = most_ordered(maria_eats_all)
    campaign.append(maria_eats)

    arnaldo_orders = person_eats_dict(path_to_file, 'arnaldo')
    arnaldo_asks_hamburguer = how_many_times('hamburguer', arnaldo_orders)
    campaign.append(arnaldo_asks_hamburguer)

    joao_orders = set(person_eats_dict(path_to_file, 'joao'))
    all_kinds = set(all_kinds_of_meals(path_to_file))
    joao_never_asks = all_kinds.difference(joao_orders)
    campaign.append(joao_never_asks)

    joao_went = set(person_days_dict(path_to_file, 'joao'))
    all_the_days = set(all_days(path_to_file))
    joao_never_went = all_the_days.difference(joao_went)
    campaign.append(joao_never_went)

    file_name = "data/mkt_campaign.txt"
    with open(file_name, "w") as text_file:
        for item in campaign:
            text_file.write("{0}\n".format(item))

    # try:
    #     assert path_to_file.endswith('.csv')
    #     with open(path_to_file) as file:
    #         arquivo = csv.reader(file, delimiter=',')

    # except AssertionError:
    #     raise ValueError("Formato invalido")
    # except FileNotFoundError:
    #     # raise ValueError(f'Arquivo {path_to_file} não encontrado')
    #     raise FileNotFoundError(f'No such file or directory: {path_to_file}')


# analyze_log("data/orders_1.csv")


# transparencia e referencias:
# refatorei a parte de encontrar a "diferença" após ver o PR
# do colega D'Andrea, solução muito mais elegante!
# https://stackoverflow.com/questions/20304824/sort-dict-by-highest-value
