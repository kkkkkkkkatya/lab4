class Dish:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} (${self.price:.2f})"


class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish: Dish):
        if dish not in self.dishes:
            self.dishes.append(dish)

    def remove_dish(self, dish: Dish):
        self.dishes.remove(dish)

    def list_dishes(self):
        return self.dishes
