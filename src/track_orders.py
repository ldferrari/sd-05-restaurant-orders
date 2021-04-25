class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({'costumer': costumer, 'order': order, 'day': day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        ordered = {}

        for val in self.orders:
            if val['costumer'] == costumer and val['order'] not in ordered:
                ordered[val['order']] = 1

            if val['costumer'] == costumer:
                ordered[val['order']] += 1

        return max(ordered, key=ordered.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        frequency = 0

        for order in self.orders:
            if order['costumer'] == costumer and order['order'] == order:
                frequency += 1

        return frequency

    def get_never_ordered_per_costumer(self, costumer):
        all_dishes = set()
        client_dishes = set()

        for order in self.orders:
            all_dishes.add(order['order'])

            if order['costumer'] == costumer:
                client_dishes.add(order['order'])

        return all_dishes.difference(client_dishes)

    def get_days_never_visited_per_costumer(self, costumer):
        restaurant_days = set()
        client_days = set()

        for order in self.orders:
            restaurant_days.add(order['day'])

            if order['costumer'] == costumer:
                client_days.add(order['day'])

        return restaurant_days.difference(client_days)

    def get_busiest_day(self):
        clients_by_day = {}

        for order in self.orders:
            if order['day'] not in clients_by_day:
                clients_by_day[order['day']] = 1

            else:
                clients_by_day[order['day']] += 1

        return max(clients_by_day, key=clients_by_day.get)

    def get_least_busy_day(self):
        clients_by_day = {}

        for order in self.orders:
            if order['day'] not in clients_by_day:
                clients_by_day[order['day']] = 1

            else:
                clients_by_day[order['day']] += 1

        return min(clients_by_day, key=clients_by_day.get)
