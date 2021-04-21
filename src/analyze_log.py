import csv


def analyze_log(path_to_file):
    with open(path_to_file, newline="") as csvfile:
        data = csv.DictReader(csvfile, fieldnames=["nome", "prato", "dia"])

        """
        Qual o prato mais pedido por 'maria'?
        Quantas vezes 'arnaldo' pediu 'hamburguer'?
        Quais pratos 'joao' nunca pediu?
        Quais dias 'joao' nunca foi na lanchonete?
        """
        
        # Array para poder fazer a o mode para saber qual
        # foi o mais pedido
        pedidos_maria = [] 
        # pedidos_arnaldo = 0
        # pedidos_joao = set()
        pratos = set()
        dias = set()

        for row in data:
            # {'hamburguer', 'coxinha', 'misto-quente', 'pizza'}
            pratos.add(row["prato"])
            # {'terça-feira', 'segunda-feira', 'sabado'}
            dias.add(row["dia"])
            if row["nome"] == "maria":
                pedidos_maria.append(row["prato"])
        print(pedidos_maria)
analyze_log('data/orders_1.csv')