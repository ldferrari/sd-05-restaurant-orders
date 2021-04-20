def mais_pedido(arr, client):
    pratos = []
    for item in arr:
        if item[0] == client:
            pratos.append(item[1])
    est = dict()
    for prato in pratos:
        est.update({prato: pratos.count(prato)})
    return est


def dias_nao_freq(arr, client):
    dias = set()
    dias_cliente = set()
    for item in arr:
        dias.add(item[2])
        if item[0] == client:
            dias_cliente.add(item[2])
    return dias - dias_cliente


def nao_pedidos(arr, client):
    pratos = set()
    pratos_cliente = set()
    for item in arr:
        pratos.add(item[1])
        if item[0] == client:
            pratos_cliente.add(item[1])
    return pratos - pratos_cliente


def dia_mais_visitado(arr):
    dias = []
    for dia in arr:
        dias.append(dia[2])
    est = dict()
    for day in dias:
        est.update({day: dias.count(day)})
    return est


class TrackOrders:
    def __init__(self):
        self.pedidos = []

    def __len__(self):
        return len(self.pedidos)

    def add_new_order(self, costumer, order, day):
        self.pedidos.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        favorito = mais_pedido(self.pedidos, costumer)
        prato_preferido = list(favorito.keys())[0]
        for prato, quantidade in favorito.items():
            if quantidade > favorito[prato_preferido]:
                prato_preferido = prato
        return prato_preferido

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        return nao_pedidos(self.pedidos, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return dias_nao_freq(self.pedidos, costumer)

    def get_busiest_day(self):
        dias = dia_mais_visitado(self.pedidos)
        melhor_dia = list(dias.keys())[0]
        for dia, quantidade in dias.items():
            if quantidade > dias[melhor_dia]:
                melhor_dia = dia
        return melhor_dia

    def get_least_busy_day(self):
        dias = dia_mais_visitado(self.pedidos)
        melhor_dia = list(dias.keys())[0]
        for dia, quantidade in dias.items():
            if quantidade < dias[melhor_dia]:
                melhor_dia = dia
        return melhor_dia
