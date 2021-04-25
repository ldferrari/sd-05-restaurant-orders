class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        ordered = {}

        for one_order in self.orders:
            if (
                one_order["costumer"] == costumer
                and one_order["order"] not in ordered
            ):
                ordered[one_order["order"]] = 1
            elif one_order["costumer"] == costumer:
                ordered[one_order["order"]] += 1

        return max(ordered, key=ordered.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        counter_order = 0

        for one_ord in self.orders:
            if one_ord['costumer'] == costumer and one_ord['order'] == order:
                counter_order += 1

        return counter_order

    def get_never_ordered_per_costumer(self, costumer):
        all_meals = set()
        ordered_by_costumer = set()

        for one_order in self.orders:
            if one_order["costumer"] == costumer:
                ordered_by_costumer.add(one_order["order"])
            all_meals.add(one_order["order"])

        return all_meals.difference(ordered_by_costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        days_by_costumer = set()

        for one_order in self.orders:
            if one_order["costumer"] == costumer:
                days_by_costumer.add(one_order["day"])
            all_days.add(one_order["day"])

        return all_days.difference(days_by_costumer)

    def get_busiest_day(self):
        busiest_day = {}

        for one_order in self.orders:
            if one_order["day"] not in busiest_day:
                busiest_day[one_order["day"]] = 1
            else:
                busiest_day[one_order["day"]] += 1

        return max(busiest_day, key=busiest_day.get)

    def get_least_busy_day(self):
        less_busy_day = {}

        for one_order in self.orders:
            if one_order["day"] not in less_busy_day:
                less_busy_day[one_order["day"]] = 1
            else:
                less_busy_day[one_order["day"]] += 1

        return min(less_busy_day, key=less_busy_day.get)
