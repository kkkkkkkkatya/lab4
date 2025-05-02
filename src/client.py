from .menu import Dish
from .order import OrderFactory


class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name

    def make_order(self, order_type: str, dishes: list[Dish]):
        return OrderFactory.create_order(order_type, dishes)