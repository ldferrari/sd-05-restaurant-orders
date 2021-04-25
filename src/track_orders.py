class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({
            'costumer': costumer,
            'order': order,
            'day': day
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_ordered_dishes = [
            order['order']
            for order in self.orders
            if order['costumer'] == costumer
        ]

        return max(most_ordered_dishes, key=most_ordered_dishes.count)

    def get_order_frequency_per_costumer(self, costumer, order):
         order_count = [
            order['order']
            for order in self.orders
            if order['costumer'] == costumer
            and order['order'] == order
        ]

        return len(order_count)

    def get_never_ordered_per_costumer(self, costumer):
        menu = set([data['order'] for data in self.orders])

        popular = set([
            data['order']
            for data in self.orders
            if data['costumer'] == costumer
        ])

        unpopular = menu.difference(popular)

        return unpopular

    def get_days_never_visited_per_costumer(self, costumer):
        days = set([data['day'] for data in self.orders])

        popular = set([
            data['day']
            for data in self.orders
            if data['costumer'] == costumer
        ])

        unpopular = days.difference(popular)

        return unpopular

    def get_busiest_day(self):
        
        days = [order['day'] for order in self.orders]

        return max(days, key=days.count)

    def get_least_busy_day(self):
        days = [order['day'] for order in self.orders]

        return min(days, key=days.count)
