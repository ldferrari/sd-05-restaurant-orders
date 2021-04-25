import csv


def analyze_log(path_to_file):
    # nao precisava do tratamento =(
    # if not path_to_file.endswith('.csv'):
    #     print(path_to_file)
    #     raise FileNotFoundError(f"No such file or directory:" + path_to_file)
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        person_set = set()
        dishes = set()
        days = set()
        persons = {}
        for entry in csv_reader:
            if not entry[0] in person_set:
                persons[entry[0]] = {
                    'pedido': {entry[1]: 1}, 'dia': set([entry[2]])}
                person_set.add(entry[0])
            else:
                if not entry[1] in persons[entry[0]]['pedido']:
                    persons[entry[0]]['pedido'].update({entry[1]: 1})
                else:
                    persons[entry[0]]['pedido'][entry[1]] += 1
                persons[entry[0]]['dia'].add(entry[2])
            dishes.add(entry[1])
            days.add(entry[2])

        maria = persons['maria']['pedido']
        mariaMax = max(maria.values())
        mariaPedidoMax = [p for p, q in maria.items() if q == mariaMax][0]

        arnaldo = persons['arnaldo']['pedido']['hamburguer']
        joao_dishes = set(persons['joao']['pedido'].keys())
        joao_no_dishes = dishes - joao_dishes

        joao_no_day = days - persons['arnaldo']['dia']

# formato da entrada
# cliente, pedido, dia
# saida em data/mkt_campaign.txt
# saida deve ter:
    with open('data/mkt_campaign.txt', 'w') as f:
        f.write(str(mariaPedidoMax))
        f.write('\n')
        f.write(str(arnaldo))
        f.write('\n')
        f.write(str(joao_no_dishes))
        f.write('\n')
        f.write(str(joao_no_day))
# Qual o prato mais pedido por 'maria'?
# Quantas vezes 'arnaldo' pediu 'hamburguer'?
# Quais pratos 'joao' nunca pediu?
# Quais dias 'joao' nunca foi na lanchonete?
# ---funcao nao retorna nada
# exemplo saida
# hamburguer
# 1
# {'pizza', 'coxinha', 'misto-quente'}
# {'sabado', 'segunda-feira'}
