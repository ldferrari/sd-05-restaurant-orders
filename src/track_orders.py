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
            if order["costumer"] == costumer:
                dishesByCostumer[order["order"]] += 1
        return Counter(dishesByCostumer).most_common(1)[0][0]

    # def get_order_frequency_per_costumer(self, costumer, order):
    #     pass

    def get_never_ordered_per_costumer(self, costumer):
        all_dishes = set()
        dishes_by_costumer = set()

        for order in self.orders:
            all_dishes.add(order["order"])
            if order["costumer"] == costumer:
                dishes_by_costumer.add(order["order"])

        return all_dishes.difference(dishes_by_costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        costumer_days = set()

        for order in self.orders:
            all_days.add(order["day"])
            if order["costumer"] == costumer:
                costumer_days.add(order["day"])

        return all_days.difference(costumer_days)

    def get_busiest_day(self):
        # Somar os dias
        orders_per_day = defaultdict(int)

        for order in self.orders:
            orders_per_day[order["day"]] += 1

        return Counter(orders_per_day).most_common(1)[0][0]

    def get_least_busy_day(self):
        orders_per_day = defaultdict(int)

        for order in self.orders:
            orders_per_day[order["day"]] += 1

        return Counter(orders_per_day).most_common()[-1][0]
