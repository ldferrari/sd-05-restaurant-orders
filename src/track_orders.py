class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        ordered_by_costumer = {}

        for registry in self.orders:
            if (
                registry["costumer"] == costumer
                and registry["order"] not in ordered_by_costumer
            ):
                ordered_by_costumer[registry["order"]] = 1
            elif registry["costumer"] == costumer:
                ordered_by_costumer[registry["order"]] += 1

        return max(ordered_by_costumer, key=ordered_by_costumer.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        order_counter = 0

        for registry in self.orders:
            if registry["costumer"] == costumer and registry["order"] == order:
                order_counter += 1

        return order_counter

    def get_never_ordered_per_costumer(self, costumer):
        every_meal = set()
        ordered_by_costumer = set()

        for registry in self.orders:
            if registry["costumer"] == costumer:
                ordered_by_costumer.add(registry["order"])
            every_meal.add(registry["order"])

        return every_meal.difference(ordered_by_costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        days_costumer_visited = set()

        for registry in self.orders:
            if registry["costumer"] == costumer:
                days_costumer_visited.add(registry["day"])
            days.add(registry["day"])

        return days.difference(days_costumer_visited)

    def get_busiest_day(self):
        days = {}

        for registry in self.orders:
            if registry["day"] not in days:
                days[registry["day"]] = 1
            else:
                days[registry["day"]] += 1

        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = {}

        for registry in self.orders:
            if registry["day"] not in days:
                days[registry["day"]] = 1
            else:
                days[registry["day"]] += 1

        return min(days, key=days.get)
