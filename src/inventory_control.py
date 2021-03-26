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

        self.inventory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }

    def add_new_order(self, costumer, order, day):
        order_ingredients = self.ingredients[order]

        for ingredient in order_ingredients:
            self.inventory[ingredient] -= 1

    def get_quantities_to_buy(self):
        ingredients_to_buy = {}
        for ingredient in self.inventory:
            ingredients_to_buy[ingredient] = (
                self.minimum_inventory[ingredient] - self.inventory[ingredient]
            )
        return ingredients_to_buy
