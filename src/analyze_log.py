import csv
from statistics import mode


def analyze_log(path_to_file):
    with open(path_to_file, newline="") as csvfile:
        data = csv.DictReader(csvfile, fieldnames=["nome", "prato", "dia"])
        
        maria_meal = []
        meals = set()
        days = set()
        arnaldo_burgers_quantity = 0
        joao_meals = set()
        joao_days = set()

        for row in data:
            meals.add(row["prato"])
            days.add(row["dia"])

            if row["nome"] == "maria":
                maria_meal.append(row["prato"])

            if row["nome"] == "arnaldo" and row["prato"] == "hamburguer":
                arnaldo_burgers_quantity += 1

            if row["nome"] == "joao":
                joao_meals.add(row["prato"])
                joao_days.add(row["dia"])

        joao_not_meals = meals.difference(joao_meals)
        joao_not_days = days.difference(joao_days)

        campaing_file = open("./data/mkt_campaign.txt", "w")

        campaing_file.write(
            f"{mode(maria_meal)}\n"
            f"{arnaldo_burgers_quantity}\n"
            f"{joao_not_meals}\n"
            f"{joao_not_days}\n"
        )

# analyze_log('data/orders_1.csv')
