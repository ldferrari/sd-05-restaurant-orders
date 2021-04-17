from collections import defaultdict
from collections import Counter

class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        dishesByCostumer = defaultdict(int)
        for order in self.orders:
            if order['costumer'] == costumer:
                dishesByCostumer[order['order']] += 1
        return (Counter(dishesByCostumer).most_common(1)[0][0])

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass


csv_parsed = [
    ["maria", "pizza", "terça-feira"],
    ["maria", "hamburguer", "terça-feira"],
    ["joao", "hamburguer", "terça-feira"],
    ["maria", "coxinha", "segunda-feira"],
    ["arnaldo", "misto-quente", "terça-feira"],
    ["jose", "hamburguer", "sabado"],
    ["maria", "hamburguer", "terça-feira"],
    ["maria", "hamburguer", "terça-feira"],
    ["joao", "hamburguer", "terça-feira"],
]

track_orders = TrackOrders()
for name, food, day in csv_parsed:
    track_orders.add_new_order(name, food, day)
most_ordered = track_orders.get_most_ordered_dish_per_costumer("maria")
assert "hamburguer" == most_ordered
