import csv


def analyze_log(path_to_file):
    maria_orders = {}
    arnaldo_counter = 0
    joao_days = set()
    joao_orders = set()
    days = set()
    catalogue = set()
    if not path_to_file.split(".")[1] == "csv":
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    with open(path_to_file) as file_input:
        for order in csv.reader(file_input, delimiter=","):
            catalogue.add(order[1])
            days.add(order[2])
            if 'maria' in order:
                if order[1] not in maria_orders:
                    maria_orders[order[1]] = 1
                else:
                    maria_orders[order[1]] += 1
            elif 'arnaldo' in order and order[1] == 'hamburguer':
                arnaldo_counter += 1
            elif 'joao' in order:
                joao_orders.add(order[1])
                joao_days.add(order[2])
    out = [
      max(maria_orders, key=maria_orders.get) + "\n",
      str(arnaldo_counter) + "\n",
      str(catalogue - joao_orders) + "\n",
      str(days - joao_days) + "\n",
    ]
    with open("data/mkt_campaign.txt", "w") as file_output:
        file_output.writelines(out)
