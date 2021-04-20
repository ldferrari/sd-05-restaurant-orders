from collections import defaultdict


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
        dishes = defaultdict(int)
        for item in self.orders:
            if item["costumer"] == costumer:
                dishes[item["order"]] += 1
        return sorted(dishes, key=dishes.get, reverse=True)[0]

    def get_order_frequency_per_costumer(self, costumer, order):
        pass


    def get_never_ordered_per_costumer(self, costumer):
        dishesByCustumer = set()
        allDishes = set()
        for item in self.orders:
            allDishes.add(item['order'])
            if item['costumer'] == costumer:
                dishesByCustumer.add(item['order'])
        return allDishes.difference(dishesByCustumer)


    def get_days_never_visited_per_costumer(self, costumer):
        daysByCustumer = set()
        allDays = set()
        for item in self.orders:
            allDays.add(item['day'])
            if item['costumer'] == costumer:
                daysByCustumer.add(item['day'])
        return allDays.difference(daysByCustumer)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
