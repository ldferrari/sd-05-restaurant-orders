class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({
            "costumer": costumer,
            "order": order,
            "day": day
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        dish_per_costumer = dict()

        for item in self.orders:
            if costumer in item['costumer']:
                if item['order'] not in dish_per_costumer:
                    dish_per_costumer[item['order']] = 1
                else:
                    dish_per_costumer[item['order']] += 1
                    return max(dish_per_costumer, key=dish_per_costumer.get)

        raise ValueError('Enter a valid user')

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        dishes = set()
        costumer_orders = set()

        for item in self.orders:
            dishes.add(item['order'])
            if costumer in item['costumer']:
                costumer_orders.add(item['order'])

        return dishes - costumer_orders

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        costumer_days = set()

        for item in self.orders:
            days.add(item['day'])
            if costumer in item['costumer']:
                costumer_days.add(item['day'])

        return days - costumer_days

    def get_busiest_day(self):
        busiest_days = dict()

        for item in self.orders:
            if item['day'] not in busiest_days:
                busiest_days[item['day']] = 1
            else:
                busiest_days[item['day']] += 1

        return max(busiest_days, key=busiest_days.get)

    def get_least_busy_day(self):
        least_busy_days = dict()

        for item in self.orders:
            if item['day'] not in least_busy_days:
                least_busy_days[item['day']] = 1
            else:
                least_busy_days[item['day']] += 1

        return min(least_busy_days, key=least_busy_days.get)
