import csv
import operator


def read_csv(file_path):
    with open(file_path, 'r') as file:
        data = csv.reader(file, delimiter=',')
        output = []
        linha = {}
        header = ["nome", "pedido", "dia"]
        for line in data:
            for index, value in enumerate(header):
                linha[value] = line[index]
            output.append(linha)
            linha = {}
        return output


def pedidos_do_cliente(file_path, cliente):
    data = read_csv(file_path)
    pedidos = dict({})
    for linha in data:
        if linha["nome"] == cliente:
            if linha["pedido"] in pedidos:
                pedidos[linha["pedido"]] += 1
            else:
                pedidos[linha["pedido"]] = 1
    return pedidos


def mais_pedido_cliente(file_path, cliente):
    pedidos = pedidos_do_cliente(file_path, cliente)
    mais_pedido = max(pedidos.items(), key=operator.itemgetter(1))[0]
    return mais_pedido


def sum_ped_food(file_path, cliente, comida):
    pedidos = pedidos_do_cliente(file_path, cliente)
    if comida in pedidos:
        return pedidos[comida]
    return 0


def set_cardapio(file_path):
    data = read_csv(file_path)
    cardapio = set()
    for linha in data:
        cardapio.add(linha["pedido"])
    return cardapio


def pratos_cliente_nao_pediu(file_path, cliente):
    cardapio = set_cardapio(file_path)
    pedidos_cliente = set(pedidos_do_cliente(file_path, cliente).keys())
    return cardapio - pedidos_cliente


def dias_cliente_apareceu(file_path, cliente):
    data = read_csv(file_path)
    dias = set()
    for linha in data:
        if linha["nome"] == cliente:
            dias.add(linha["dia"])
    return dias


def dias_cliente_nao_apareceu(file_path, cliente):
    diasCliente = dias_cliente_apareceu(file_path, cliente)
    diasAberto = set({"sabado", "segunda-feira", "terça-feira"})
    return diasAberto - diasCliente


def analyze_log(path_to_file):
    resultado = []
    resultado.append(mais_pedido_cliente(path_to_file, "maria"))
    resultado.append(sum_ped_food(path_to_file, "arnaldo", "hamburguer"))
    resultado.append(pratos_cliente_nao_pediu(path_to_file, "joao"))
    resultado.append(dias_cliente_nao_apareceu(path_to_file, "joao"))
    print(resultado)
    with open("data/mkt_campaign.txt", "w") as text_file:
        for value in resultado:
            text_file.write(str(value) + "\n")
