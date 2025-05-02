from src.menu import Dish
from src.order import OrderFactory, RegularOrder, BulkOrder

def test_regular_order_total_price():
    dish = Dish("Soup", 5.0)
    order = OrderFactory.create_order("regular", [dish])
    assert isinstance(order, RegularOrder)
    assert order.total_price() == 5.0

def test_bulk_order_discount():
    dish = Dish("Salad", 10.0)
    order = OrderFactory.create_order("bulk", [dish])
    assert isinstance(order, BulkOrder)
    assert order.total_price() == 9.0  # 10% discount

def test_empty_order_total_price():
    order = OrderFactory.create_order("regular", [])
    assert order.total_price() == 0.0

def test_order_with_multiple_dishes():
    dishes = [Dish("Sushi", 12.0), Dish("Tempura", 8.0)]
    order = OrderFactory.create_order("regular", dishes)
    assert order.total_price() == 20.0
