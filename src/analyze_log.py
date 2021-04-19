import csv
from collections import defaultdict

# 1. Em cada function, transformar orders_1.csv em objeto relevante

# 2. Functions necessárias para achar os 4 elementos pedidos

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


# 3. Achar os 4 elementos pedidos
# 3.1 Prato mais pedido por cliente ('maria')
def most_ordered_dish_by_customer(path_to_file, customer):
    dish = list(most_ordered_dishes(path_to_file, customer).keys())[0]
    return dish
    # formato retornado: hamburger

# 3.2 Contar vezes que cliente ('arnaldo') pediu prato ('hamburguer')
def count_dishes_by_customer(path_to_file, customer, dish):
    count_dish = most_ordered_dishes(path_to_file, customer)[dish]
    return count_dish

# 3.3 Pratos que cliente ('joao') nunca pediu
def get_never_ordered(path_to_file, customer):
    return get_all_dishes(path_to_file).difference(dishes_by_customer(path_to_file, customer))

# 3.4 Dias que cliente ('joao') nunca foi na lanchonete
def get_never_went(path_to_file, customer):
    return get_all_days(path_to_file).difference(days_by_customer(path_to_file, customer))

# 4. Mandar as respostas no arquivo data/mkt_campaign.txt
def analyze_log(path_to_file):
    final_text = []
    final_text.append(most_ordered_dish_by_customer('data/orders_1.csv', 'maria'))
    final_text.append(count_dishes_by_customer('data/orders_1.csv', 'arnaldo', 'hamburguer'))
    final_text.append(get_never_ordered('data/orders_1.csv', 'joao'))
    final_text.append(get_never_went('data/orders_1.csv', 'joao'))
    # print(final_text)
    # ['hamburguer', 1, {'pizza', 'coxinha', 'misto-quente'}, {'segunda-feira', 'sabado'}]
    file_path = "data/mkt_campaign.txt"
    with open(file_path, "w") as final_file:
        for element in final_text:
            final_file.write(str(element) + "\n")
            # https://stackoverflow.com/questions/37289951/how-to-write-to-a-csv-line-by-line
    # without try except


if __name__ == "__main__":
    # print(days_by_customer('data/orders_1.csv', 'joao'))
    # print(dishes_by_customer('data/orders_1.csv', 'joao'))
    # print(most_ordered_dish_by_customer('data/orders_1.csv', 'maria'))
    # print(count_dishes_by_customer('data/orders_1.csv', 'arnaldo', 'hamburguer'))
    # print(get_never_ordered('data/orders_1.csv', 'joao'))
    # print(get_never_went('data/orders_1.csv', 'joao'))
    print(analyze_log('data/orders_1.csv'))
