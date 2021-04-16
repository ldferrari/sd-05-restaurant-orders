import csv
from collections import defaultdict


def findDishesQnt(costumer, filepath):
    dishes = defaultdict(int)
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            if row[0] == costumer:
                dishes[row[1]] += 1
    return dict(dishes)


def findMostFrequentMeal(meals):
    meals = list(meals.items())
    mostFrequentTuple = meals[0]

    for meal in meals:
        mostFrequentQnt = mostFrequentTuple[1]
        mealQnt = meal[1]
        if mealQnt > mostFrequentQnt:
            mostFrequentTuple = meal

    return mostFrequentTuple[0]


def write_campaign(filepath, infos):

    with open(filepath, "w") as text_file:
        for info in infos:
            text_file.write("{0}\n".format(info))


def findQuantity(meals, meal):
    return meals[meal]


def getAllDishes(filepath):
    dishes = defaultdict(int)
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            dishes[row[1]] += 1
    return dict(dishes)


def getAllDays(filepath):
    days = set()
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            days.add(row[2])

    return days


def costumerWentAt(costumer, filepath):
    days = set()
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            if row[0] == costumer:
                days.add(row[2])

    return days


def analyze_log(path_to_file):
    to_write_campaign = []
    campaign_file = "data/mkt_campaign.txt"

    maria_dishes = findDishesQnt("maria", path_to_file)
    most_frequent_maria_dish = findMostFrequentMeal(maria_dishes)

    to_write_campaign.append(most_frequent_maria_dish)

    arnaldo_dishes = findDishesQnt("arnaldo", path_to_file)
    quantityPerFood = findQuantity(arnaldo_dishes, "hamburguer")
    to_write_campaign.append(quantityPerFood)

    joao_dishes = set(findDishesQnt("joao", path_to_file))
    all_dishes = set(getAllDishes(path_to_file))
    dishes_difference = all_dishes.difference(joao_dishes)
    to_write_campaign.append(dishes_difference)

    joao_days = set(costumerWentAt("joao", path_to_file))
    all_days = set(getAllDays(path_to_file))
    days_difference = all_days.difference(joao_days)

    to_write_campaign.append(days_difference)

    write_campaign(campaign_file, to_write_campaign)
    # write_campaign(to_write_campaign)
    # print(all_days)
    # print(joao_days)


analyze_log("data/orders_1.csv")
