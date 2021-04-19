import csv

# 1. Em cada function, transformar orders_1.csv em objeto relevante

# 2. Functions necessárias para achar os 4 elementos pedidos
# def get_all_dishes()
# def get_all_days()

# 3. Achar os 4 elementos pedidos

# 3.1 Prato mais pedido por cliente ('maria')

def dishes_by_customer(path_to_file, customer):
    dishes_customer = set()
    with open(path_to_file) as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] == customer:
                dishes_customer.add(line[1])
    return dishes_customer

def most_ordered_dish_by_customer(path_to_file, customer):
    # cannot be a set because each element would be unique
    print(customer)
    
# 3.2 Vezes que cliente ('arnaldo') pediu prato ('hamburguer')
def count_dishes_by_customer(path_to_file, customer):statu
    print(customer)

# 3.3 Pratos que cliente ('joao') nunca pediu
# Comparando os que pediu com a lista inteira de pratos

# 3.4 Dias que cliente ('joao') nunca foi na lanchonete
# Comparando os que estava com a lista inteira de dias

# 4. Mandar as respostas no arquivo data/mkt_campaign.txt
def analyze_log(path_to_file):
    raise NotImplementedError
    # final_text = []
    # append each 4 pertinent functions with correct name on it
    # final_text.append()
    # print final_text to understand how to format it
    # with open("data/mkt_campaign.txt", "w") as final_file:
    #     for element in final_text:
    #         final_file.write(here format answer / line)


if __name__ == "__main__":
    print(dishes_by_customer('data/orders_1.csv', 'maria'))
