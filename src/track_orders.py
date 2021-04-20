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
        # print(dishes_by_customer)
        sorting = sorted(dishes_cstmer, key=dishes_cstmer.get, reverse=True)
        # print(dishes_sorted)
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
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
