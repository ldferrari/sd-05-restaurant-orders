import csv

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


# 3. Achar os 4 elementos pedidos
# 3.1 Prato mais pedido por cliente ('maria')
def most_ordered_dish_by_customer(path_to_file, customer):
    # cannot be a set because each element would be unique
    print(customer)
    

# 3.2 Contar vezes que cliente ('arnaldo') pediu prato ('hamburguer')
def count_dishes_by_customer(path_to_file, customer):
    print(customer)


# 3.3 Pratos que cliente ('joao') nunca pediu
def get_never_ordered(path_to_file, customer):
    return get_all_dishes(path_to_file).difference(dishes_by_customer(path_to_file, customer))

# 3.4 Dias que cliente ('joao') nunca foi na lanchonete
def get_never_went(path_to_file, customer):
    return get_all_days(path_to_file).difference(days_by_customer(path_to_file, customer))


# 4. Mandar as respostas no arquivo data/mkt_campaign.txt
def analyze_log(path_to_file):
    raise NotImplementedError
    final_text = []
    # falta 1 2
    final_text.append(get_never_ordered('data/orders_1.csv', 'joao'))
    final_text.append(get_never_went('data/orders_1.csv', 'joao'))
    # print final_text to understand how to format it
    # with open("data/mkt_campaign.txt", "w") as final_file:
    #     for element in final_text:
    #         final_file.write(here format answer / line)


if __name__ == "__main__":
    # print(days_by_customer('data/orders_1.csv', 'joao'))
    # print(dishes_by_customer('data/orders_1.csv', 'joao'))
    print(get_never_ordered('data/orders_1.csv', 'joao'))
    print(get_never_went('data/orders_1.csv', 'joao'))
