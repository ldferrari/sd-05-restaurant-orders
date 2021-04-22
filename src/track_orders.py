def get_dict_food_frequency_costumer(self, costumer):
    comida_contador = {}
    for pedido in self.pedidos:
        pessoa = pedido["costumer"]
        comida = pedido["order"]
        if (pessoa == costumer):
            if (comida not in comida_contador):
                comida_contador[comida] = 1
            else:
                comida_contador[comida] += 1
    return comida_contador


def get_existing_food_plates(self):
    pratos = set()
    for pedido in self.pedidos:
        pratos.add(pedido["order"])
    return pratos


def get_existing_food_plates_costumer(self, costumer):
    pratos = set()
    for pedido in self.pedidos:
        pessoa = pedido["costumer"]
        if(pessoa == costumer):
            pratos.add(pedido["order"])
    return pratos


def get_working_days(self):
    dias = set()
    for pedido in self.pedidos:
        dias.add(pedido["day"])
    return dias


def get_days_visited_costumer(self, costumer):
    dias = set()
    for pedido in self.pedidos:
        pessoa = pedido["costumer"]
        if (pessoa == costumer):
            dias.add(pedido["day"])
    return dias


def get_dict_frequency_days(self):
    dia_contador = {}
    for pedido in self.pedidos:
        dia = pedido["day"]
        if (dia not in dia_contador):
            dia_contador[dia] = 1
        else:
            dia_contador[dia] += 1
    return dia_contador


class TrackOrders:
    def __init__(self):
        self.pedidos = []

    def __len__(self):
        return len(self.pedidos)

    def add_new_order(self, costumer, order, day):
        self.pedidos.append({
            "costumer": costumer,
            "order": order,
            "day": day
            })

    def get_most_ordered_dish_per_costumer(self, costumer):
        comida_contador = get_dict_food_frequency_costumer(self, costumer)
        return max(comida_contador, key=comida_contador.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        comida_contador = get_dict_food_frequency_costumer(self, costumer)
        return comida_contador[order]

    def get_never_ordered_per_costumer(self, costumer):
        pratos = get_existing_food_plates(self)
        pratos_consumidor = get_existing_food_plates_costumer(self, costumer)
        return pratos.difference(pratos_consumidor)

    def get_days_never_visited_per_costumer(self, costumer):
        dias_funcionamento = get_working_days(self)
        dias_visitados_consumidor = get_days_visited_costumer(self, costumer)
        return dias_funcionamento.difference(dias_visitados_consumidor)

    def get_busiest_day(self):
        dias_contador = get_dict_frequency_days(self)
        return max(dias_contador, key=dias_contador.get)

    def get_least_busy_day(self):
        dias_contador = get_dict_frequency_days(self)
        return min(dias_contador, key=dias_contador.get)

# https://stackoverflow.com/questions/15114023/using-len-and-def-len-self-to-build-a-class
