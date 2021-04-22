import csv


def dict_comida_numero_pedidos_pessoa(path_to_file, pessoa_escolhida):
    with open(path_to_file) as file:
        pedidos = csv.reader(file)
        comida_contador = {}
        for linha in pedidos:
            pessoa = linha[0]
            comida = linha[1]
            if (pessoa == pessoa_escolhida):
                if (comida not in comida_contador):
                    comida_contador[comida] = 1
                else:
                    comida_contador[comida] += 1

        return comida_contador


def prato_mais_pedido_pessoa(path, pessoa_escolhida):
    comida_contador = dict_comida_numero_pedidos_pessoa(path, pessoa_escolhida)
    max_key = max(comida_contador, key=comida_contador.get)
    return max_key


def quantas_vezes_pediu_tipo_comida(path, pessoa_escolhida, comida):
    comida_contador = dict_comida_numero_pedidos_pessoa(path, pessoa_escolhida)
    return comida_contador[comida]


def pratos_existentes(path):
    pratos = set()
    with open(path) as file:
        pedidos = csv.reader(file)
        for linha in pedidos:
            pratos.add(linha[1])
    return pratos


def pratos_pedidos_pessoa(path, pessoa_escolhida):
    pratos = set()
    with open(path) as file:
        pedidos = csv.reader(file)
        for linha in pedidos:
            pessoa = linha[0]
            if (pessoa == pessoa_escolhida):
                pratos.add(linha[1])
    return pratos


def dias_funcionamento(path):
    dias = set()
    with open(path) as file:
        pedidos = csv.reader(file)
        for linha in pedidos:
            dias.add(linha[2])
    return dias


def dias_pessoa_fez_pedido(path, pessoa_escolhida):
    dias = set()
    with open(path) as file:
        pedidos = csv.reader(file)
        for linha in pedidos:
            pessoa = linha[0]
            if (pessoa == pessoa_escolhida):
                dias.add(linha[2])
    return dias


def salvar_array_em_arquivo(array, path):
    with open(path, "w") as file:
        for item in array:
            file.write(str(item) + "\n")


def analyze_log(path_to_file):
    comida_mais_pedida_maria = prato_mais_pedido_pessoa(path_to_file, "maria")

    vezes_arnaldo_pediu_hamburger = quantas_vezes_pediu_tipo_comida(
        path_to_file, "arnaldo", "hamburguer"
        )

    pratos = pratos_existentes(path_to_file)
    pratos_pedidos_joao = pratos_pedidos_pessoa(path_to_file, "joao")
    pratos_nao_pedidos_joao = pratos.difference(pratos_pedidos_joao)

    dias_joao_foi_lanchonete = dias_pessoa_fez_pedido(path_to_file, "joao")
    dias_lanchonete_funcionou = dias_funcionamento(path_to_file)
    dias_joao_nao_foi_lanchonete = dias_lanchonete_funcionou.difference(
        dias_joao_foi_lanchonete
        )

    analise = []
    analise.append(comida_mais_pedida_maria)
    analise.append(vezes_arnaldo_pediu_hamburger)
    analise.append(pratos_nao_pedidos_joao)
    analise.append(dias_joao_nao_foi_lanchonete)
    salvar_array_em_arquivo(analise, "data/mkt_campaign.txt")

# # # salvar em: data/mkt_campaign.txt
# https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python
# https://www.geeksforgeeks.org/reading-writing-text-files-python/
