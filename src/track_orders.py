from collections import defaultdict


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        dishes_cstmer = defaultdict(int)
        for order in self.orders:
            if order["costumer"] == costumer:
                dishes_cstmer[order["order"]] += 1
        # print(dishes_cstmer)
        sorting = sorted(dishes_cstmer, key=dishes_cstmer.get, reverse=True)
        # print(sorting)
        most_ordered_dish = sorting[0]
        return most_ordered_dish

    # did not understand from function name what it wants
    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        all_dishes = set()
        customer_dishes = set()
        for order in self.orders:
            all_dishes.add(order["order"])
            if order["costumer"] == costumer:
                customer_dishes.add(order["order"])
        never_ordered_dish = all_dishes.difference(customer_dishes)
        return never_ordered_dish

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        customer_days = set()
        for order in self.orders:
            all_days.add(order["day"])
            if order["costumer"] == costumer:
                customer_days.add(order["day"])
        never_went_days = all_days.difference(customer_days)
        return never_went_days

    def get_busiest_day(self):
        days = defaultdict(int)
        for order in self.orders:
            if order["day"] not in days:
                days[order["day"]] = 1
            else:
                days[order['day']] += 1
        # print(days)
        sorting = sorted(days, key=days.get, reverse=True)
        busiest_day = sorting[0]
        return busiest_day

    def get_least_busy_day(self):
        # same with different sorting
        days = defaultdict(int)
        for order in self.orders:
            if order["day"] not in days:
                days[order["day"]] = 1
            else:
                days[order['day']] += 1
        sorting = sorted(days, key=days.get)
        least_busy_day = sorting[0]
        return least_busy_day
