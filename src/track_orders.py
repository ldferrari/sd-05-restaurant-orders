class TrackOrders:

    def __init__(self):
        self.orders = []
        self.person_set = set()
        self.dishes = set()
        self.days = set()
        self.persons = {}
        self.work_per_day = {}

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.dishes.add(order)
        self.days.add(day)

        if day not in self.work_per_day:
            self.work_per_day[day] = 1
        else:
            self.work_per_day[day] += 1

        if costumer not in self.person_set:
            self.persons[costumer] = {
                'pedido': {order: 1}, 'dia': set([day])}
            self.person_set.add(costumer)
        else:
            if order not in self.persons[costumer]['pedido']:
                self.persons[costumer]['pedido'].update({order: 1})
            else:
                self.persons[costumer]['pedido'][order] += 1
            self.persons[costumer]['dia'].add(day)
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        data = self.persons[costumer]['pedido']
        maxData = max(data.values())
        return [item for item, qty in data.items() if qty == maxData][0]

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        return self.dishes - set(self.persons[costumer]['pedido'].keys())

    def get_days_never_visited_per_costumer(self, costumer):
        return self.days - self.persons[costumer]['dia']

    def get_busiest_day(self):
        data = self.work_per_day
        maxData = max(data.values())
        return [item for item, qty in data.items() if qty == maxData][0]

    def get_least_busy_day(self):
        data = self.work_per_day
        maxData = min(data.values())
        return [item for item, qty in data.items() if qty == maxData][0]
