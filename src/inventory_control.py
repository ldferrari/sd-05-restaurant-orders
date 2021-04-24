class InventoryControl:
    def __init__(self):
        self.ingredients = {
            'hamburguer': ['pao', 'carne', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }

        self.minimum_inventory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }
        
        self.to_buy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, costumer, order, day):
        ingredients = self.ingredients.get(order)
        for ingredient in ingredients:
            qtd = self.minimum_inventory.get(ingredient)
            self.to_buy[ingredient] += 1
            if qtd == 0:
                return False
            self.minimum_inventory[ingredient] = qtd - 1

    def get_quantities_to_buy(self):
        return self.to_buy
    
    def get_available_dishes(self):
        dishes =  set(self.ingredients.keys())
        for dish in self.ingredients.keys():
            for ingredient in self.ingredients.get(dish):
                if self.minimum_inventory.get(ingredient) <= self.to_buy.get(ingredient):
                    dishes.remove(dish)
                    break
        return dishes
