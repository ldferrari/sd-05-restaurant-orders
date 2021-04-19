import csv


def lista_pratos(arr, client):
    pratos = []
    for item in arr:
        if item[0] == client:
            pratos.append(item[1])
    est = dict()
    for prato in pratos:
        est.update({prato: pratos.count(prato)})
    return est


def nao_pedidos(arr, client):
    pratos = set()
    pratos_cliente = set()
    for item in arr:
        pratos.add(item[1])
        if item[0] == client:
            pratos_cliente.add(item[1])
    return pratos - pratos_cliente


def dias_nao_freq(arr, client):
    dias = set()
    dias_cliente = set()
    for item in arr:
        dias.add(item[2])
        if item[0] == client:
            dias_cliente.add(item[2])
    return dias - dias_cliente


def escrever_arq(content, filepath):
    with open(filepath, 'a') as file:
        for item in content:
            file.write(str(item) + '\n')


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        filepath_reader = list(csv.reader(file, delimiter=","))
    maria = lista_pratos(filepath_reader, 'maria')
    prato_maria = list(maria.keys())[0]
    for prato, quantidade in maria.items():
        if quantidade > maria[prato_maria]:
            prato_maria = prato
    arnaldo_burgao = lista_pratos(filepath_reader, 'arnaldo')['hamburguer']
    joao_nao = nao_pedidos(filepath_reader, 'joao')
    dias_joao = dias_nao_freq(filepath_reader, 'joao')
    content = [prato_maria, arnaldo_burgao, joao_nao, dias_joao]
    escrever_arq(content, 'data/mkt_campaign.txt')
