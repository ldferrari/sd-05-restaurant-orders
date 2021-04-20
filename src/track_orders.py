class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        count_dishes = dict()
        for item in self.orders:
            if costumer in item['costumer']:
                if item['order'] not in count_dishes:
                    count_dishes[item['order']] = 1
                else:
                    count_dishes[item['order']] += 1
                    return max(count_dishes, key=count_dishes.get)
        raise ValueError('Enter a valid user')

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        dishes_set = set()
        costumer_orders = set()

        for item in self.orders:
            dishes_set.add(item['order'])
            if costumer in item['costumer']:
                costumer_orders.add(item['order'])

        return dishes_set - costumer_orders

    def get_days_never_visited_per_costumer(self, costumer):
        days_set = set()
        costumer_days = set()

        for item in self.orders:
            days_set.add(item['day'])
            if costumer in item['costumer']:
                costumer_days.add(item['day'])

        return days_set - costumer_days

    def get_busiest_day(self):
        each_day_quantity = dict()
        for item in self.orders:
            if item['day'] not in each_day_quantity:
                each_day_quantity[item['day']] = 1
            else:
                each_day_quantity[item['day']] += 1
        return max(each_day_quantity, key=each_day_quantity.get)

    def get_least_busy_day(self):
        each_day_quantity = dict()
        for item in self.orders:
            if item['day'] not in each_day_quantity:
                each_day_quantity[item['day']] = 1
            else:
                each_day_quantity[item['day']] += 1
        return min(each_day_quantity, key=each_day_quantity.get)
