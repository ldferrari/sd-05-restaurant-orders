from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []
        self.menu = set()
        self.open_days = set()

    def __len__(self):
        return len(self.orders)

    def filter_order(self, costumer):
        return [order for order in self.orders
                if costumer in order]

    def count_costumer_order(self, orders):
        return dict(Counter([item for _, item, _ in orders]))

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])
        self.menu = {item for _, item, _ in self.orders}
        self.open_days = {day for _, _, day in self.orders}

    def get_most_ordered_dish_per_costumer(self, costumer):
        customer_order = self.filter_order(costumer)
        count = self.count_costumer_order(customer_order)
        return max(count, key=count.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        ordered = self.filter_order(costumer)
        ordered = {order for _, order, _ in ordered}
        return self.menu - ordered

    def get_days_never_visited_per_costumer(self, costumer):
        day = self.filter_order(costumer)
        day = {day for _, _, day in day}
        return self.open_days - day

    def get_busiest_day(self):
        count = dict(Counter([day for _, _, day in self.orders]))
        return max(count, key=count.get)

    def get_least_busy_day(self):
        count = dict(Counter([day for _, _, day in self.orders]))
        return min(count, key=count.get)
