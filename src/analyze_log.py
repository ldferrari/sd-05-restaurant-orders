import csv
from collections import defaultdict


def getAllDishes(filepath):
    dishes = set()
    with open(filepath) as file:
        reader = csv.reader(file)

        for row in reader:
            dishes.add(row[1])
    return dishes


def getDishesByCostumer(filepath, costumer):
    dishes = set()
    with open(filepath) as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == costumer:
                dishes.add(row[1])
    return dishes


def getAllDays(filepath):
    days = set()
    with open(filepath) as file:
        reader = csv.reader(file)

        for row in reader:
            days.add(row[2])
    return days


def getDaysByCostumer(filepath, costumer):
    days = set()
    with open(filepath) as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == costumer:
                days.add(row[2])
    return days


def getMostOrderedMeal(filepath, costumer):
    dishes = defaultdict(int)
    with open(filepath) as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == costumer:
                dishes[row[1]] += 1
    return dict(dishes)


def analyze_log(path_to_file):
    result = []
    result.append(list(getMostOrderedMeal(path_to_file, 'maria').keys())[0])
    result.append(getMostOrderedMeal(path_to_file, 'arnaldo')['hamburguer'])
    result.append(
      getAllDishes(path_to_file)
      .difference(getDishesByCostumer(path_to_file, 'joao')))
    result.append(
      getAllDays(path_to_file)
      .difference(getDaysByCostumer(path_to_file, 'joao')))

    print(result)
    with open("data/mkt_campaign.txt", "w") as text_file:
        for value in result:
            text_file.write(str(value) + "\n")
