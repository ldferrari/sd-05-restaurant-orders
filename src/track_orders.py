from src.analyze_log import most_requested
from src.analyze_log import never_did_it


class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return most_requested(self.orders, costumer)

    def get_order_frequency_per_costumer(self, client, request):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        return never_did_it(self.orders, costumer, 1)

    def get_days_never_visited_per_costumer(self, costumer):
        return never_did_it(self.orders, costumer, 2)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
