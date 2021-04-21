import csv
from statistics import mode


def analyze_log(path_to_file):
    with open(path_to_file, newline="") as csvfile:
        data = csv.DictReader(csvfile, fieldnames=["nome", "prato", "dia"])

        """
        Quais pratos 'joao' nunca pediu?
        Quais dias 'joao' nunca foi na lanchonete?
        """
        
        # Array para poder fazer a o mode para saber qual
        # foi o mais pedido
        pedidos_maria = [] 
        hamburguer_arnaldo = 0
        pratos = set()
        dias = set()
        pratos_joao = set()

        for row in data:
            # {'hamburguer', 'coxinha', 'misto-quente', 'pizza'}
            pratos.add(row["prato"])
            # {'terça-feira', 'segunda-feira', 'sabado'}
            dias.add(row["dia"])
            # Qual o prato mais pedido por 'maria'?
            if row["nome"] == "maria":
                pedidos_maria.append(row["prato"])
            # Quantas vezes 'arnaldo' pediu 'hamburguer'?
            if row["nome"] == "arnaldo" and row["prato"] == "hamburguer":
                hamburguer_arnaldo += 1
            if row["nome"] == "joao":
                pratos_joao.add(row["prato"])
            # Quais pratos 'joao' nunca pediu?

        joao_nunca_pediu = pratos.difference(pratos_joao)
        
        campaign_text = open("./data/mkt_campaign.txt", "w")
        campaign_text.write(
            f"{mode(pedidos_maria)}\n"
            f"{hamburguer_arnaldo}\n"
            f"{joao_nunca_pediu}\n"
        )
analyze_log('data/orders_1.csv')