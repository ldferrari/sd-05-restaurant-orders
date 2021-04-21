import operator


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        pedidos = dict({})
        for order in self.orders:
            if order["costumer"] == costumer:
                if order["order"] in pedidos:
                    pedidos[order["order"]] += 1
                else:
                    pedidos[order["order"]] = 1
        mais_pedido = max(pedidos.items(), key=operator.itemgetter(1))[0]
        return mais_pedido

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        cardapio = set()
        pedidos_cliente = set()
        for order in self.orders:
            cardapio.add(order["order"])
            if order["costumer"] == costumer:
                pedidos_cliente.add(order["order"])
        return cardapio - pedidos_cliente

    def get_days_never_visited_per_costumer(self, costumer):
        dias_funcionando = set()
        dias_cliente_apareceu = set()
        for order in self.orders:
            dias_funcionando.add(order["day"])
            if order["costumer"] == costumer:
                dias_cliente_apareceu.add(order["day"])
        return dias_funcionando - dias_cliente_apareceu

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
