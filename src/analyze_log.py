import csv
import operator


PATH = "data/orders_1.csv"


def read_csv(file_path):
    try:
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
    except FileNotFoundError:
        raise ValueError("File not found")


def pedidos_do_cliente(cliente):
    data = read_csv(PATH)
    pedidos = dict({})
    for linha in data:
        if linha["nome"] == cliente:
            if linha["pedido"] in pedidos:
                pedidos[linha["pedido"]] += 1
            else:
                pedidos[linha["pedido"]] = 1
    return pedidos


def mais_pedido_cliente(cliente):
    pedidos = pedidos_do_cliente(cliente)
    mais_pedido = max(pedidos.items(), key=operator.itemgetter(1))[0]
    return mais_pedido


def soma_vezes_pediu_tal_comida(cliente, comida):
    pedidos = pedidos_do_cliente(cliente)
    if comida in pedidos:
        return pedidos[comida]
    return 0


def set_cardapio():
    data = read_csv(PATH)
    cardapio = set()
    for linha in data:
        cardapio.add(linha["pedido"])
    return cardapio


def pratos_cliente_nao_pediu(cliente):
    cardapio = set_cardapio()
    pedidos_cliente = set(pedidos_do_cliente(cliente).keys())
    return cardapio - pedidos_cliente


def dias_cliente_apareceu(cliente):
    data = read_csv(PATH)
    dias = set()
    for linha in data:
        if linha["nome"] == cliente:
            dias.add(linha["dia"])
    return dias


def dias_cliente_nao_apareceu(cliente):
    diasCliente = dias_cliente_apareceu(cliente)
    diasAberto = set({"sabado", "segunda-feira", "terça-feira"})
    return diasAberto - diasCliente


def analyze_log(path_to_file):
    resultado = []
    resultado.append(mais_pedido_cliente("maria"))
    resultado.append(soma_vezes_pediu_tal_comida("arnaldo", "hamburguer"))
    resultado.append(pratos_cliente_nao_pediu("joao"))
    resultado.append(dias_cliente_nao_apareceu("joao"))
    print(resultado)
    with open("data/mkt_campaign.txt", "w") as text_file:
        for value in resultado:
            text_file.write(str(value) + "\n")


analyze_log(PATH)


print(mais_pedido_cliente("maria"))
print(soma_vezes_pediu_tal_comida("arnaldo", "hamburguer"))
print(pratos_cliente_nao_pediu("joao"))
print(dias_cliente_nao_apareceu("joao"))
