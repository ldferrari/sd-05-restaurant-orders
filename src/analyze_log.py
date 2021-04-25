import csv


def most_something_by_person(persons, person, something):
    data = persons[person][something]
    maxData = max(data.values())
    return [item for item, quantity in data.items() if quantity == maxData][0]


def saida_arquivo(dado1, dado2, dado3, dado4, ):
    with open('data/mkt_campaign.txt', 'w') as f:
        f.write(str(dado1))
        f.write('\n')
        f.write(str(dado2))
        f.write('\n')
        f.write(str(dado3))
        f.write('\n')
        f.write(str(dado4))


def analyze_log(path_to_file):
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        person_set = set()
        dishes = set()
        days = set()
        persons = {}
        for entry in csv_reader:
            dishes.add(entry[1])
            days.add(entry[2])
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

        mariaPedidoMax = most_something_by_person(persons, 'maria', 'pedido')
        arnaldo = persons['arnaldo']['pedido']['hamburguer']
        joao_no_dishes = dishes - set(persons['joao']['pedido'].keys())
        joao_no_day = days - persons['arnaldo']['dia']

    saida_arquivo(mariaPedidoMax, arnaldo, joao_no_dishes, joao_no_day)
