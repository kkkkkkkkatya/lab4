from abc import ABC, abstractmethod
from .menu import Dish


class Order(ABC):
    def __init__(self, dishes: list[Dish]):
        self.dishes = dishes
        self.status = 'New'

    def total_price(self):
        return sum(d.price for d in self.dishes)

    def __repr__(self):
        return f"Order({[d.name for d in self.dishes]}) - {self.status}"


class RegularOrder(Order):
    pass


class BulkOrder(Order):
    def __init__(self, dishes: list[Dish]):
        super().__init__(dishes)
        self.discount = 0.1  # 10% discount

    def total_price(self):
        return super().total_price() * (1 - self.discount)


class OrderFactory:
    @staticmethod
    def create_order(order_type: str, dishes: list[Dish]) -> Order:
        if order_type == "bulk":
            return BulkOrder(dishes)
        return RegularOrder(dishes)
