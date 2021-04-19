class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        meals = {}
        for order in self.orders:
            if order['costumer'] == costumer:
                if order['order'] not in meals:
                    meals[order['order']] = 1
                else:
                    meals[order['order']] += 1
        highest = sorted(meals, key=meals.get, reverse=True)
        return highest[0]

    # não avaliado?
    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        costumer_meals = set()
        all_meals = set()
        for order in self.orders:
            if order['costumer'] == costumer:
                costumer_meals.add(order['order'])
                all_meals.add(order['order'])
            else:
                all_meals.add(order['order'])

        return all_meals.difference(costumer_meals)

    def get_days_never_visited_per_costumer(self, costumer):
        costumer_days = set()
        all_days = set()
        for order in self.orders:
            if order['costumer'] == costumer:
                costumer_days.add(order['day'])
                all_days.add(order['day'])
            else:
                all_days.add(order['day'])

        return all_days.difference(costumer_days)

    def get_busiest_day(self):
        all_days = {}
        for order in self.orders:
            if order['day'] not in all_days:
                all_days[order['day']] = 1
            else:
                all_days[order['day']] += 1
        return sorted(all_days, key=all_days.get, reverse=True)[0]

    def get_least_busy_day(self):
        all_days = {}
        for order in self.orders:
            if order['day'] not in all_days:
                all_days[order['day']] = 1
            else:
                all_days[order['day']] += 1
        return sorted(all_days, key=all_days.get)[0]

# transparencia, não estava entendendo o que precisavamos implementar no
# def __len__(self): então olhei no PR do D'Andrea
