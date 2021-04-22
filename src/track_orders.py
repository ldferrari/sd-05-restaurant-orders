from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    # 2.1 - Será validado se, ao instanciar a classe TrackOrders
    # pela primeira vez, o método retorna a quantidade de pedidos
    # é igual a zero.
    def __len__(self):
        return len(self.orders)

    # 2.2 - Será validado se, ao executar o método add_new_order,
    # o método deve adicionar um pedido.
    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    # 2.3 - Será validado se, ao executar get_most_ordered_dish_per_costumer,
    # o método retorna o prato mais pedido.
    def get_most_ordered_dish_per_costumer(self, costumer):
        dish_per_costumer = []
        for costumer_name, prato, _ in self.orders:
            if costumer_name == costumer:
                dish_per_costumer.append([costumer_name, prato])

        resp = Counter([order[1] for order in dish_per_costumer])
        return resp.most_common(1)[0][0]

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    # 2.4 - Será validado se, ao executar
    # get_never_ordered_per_costumer, o método retorna o
    # pedido que o cliente nunca fez.
    def get_never_ordered_per_costumer(self, costumer):
        pratos = set([order[1] for order in self.orders])
        cust_pratos = set(
            [order[1] for order in self.orders if order[0] == costumer]
        )

        return pratos.difference(cust_pratos)

    # 2.5 - Será validado se, ao executar get_days_never_visited_per_costumer,
    # o método retorna o dias que o cliente nunca visitou.
    def get_days_never_visited_per_costumer(self, costumer):
        pass

    # 2.6 - Será validado se, ao executar o método get_busiest_day,
    # o método retorna o dia mais movimentado.
    def get_busiest_day(self):
        pass

    # 2.7 - Será validado se, ao executar o método get_least_busy_day,
    # o método retorna o dia menos movimentado.
    def get_least_busy_day(self):
        pass
