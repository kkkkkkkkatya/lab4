from src.database import OrdersDatabase
from src.menu import Dish
from src.order import OrderFactory


def test_database_singleton_and_add():
    db1 = OrdersDatabase()
    db2 = OrdersDatabase()
    assert db1 is db2  # singleton test

    dish = Dish("Cake", 6.0)
    order = OrderFactory.create_order("regular", [dish])
    db1.add_order(order)
    assert order in db2.get_orders()
