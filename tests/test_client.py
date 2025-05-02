from src.menu import Dish
from src.client import Client
from src.order import RegularOrder

def test_client_makes_order():
    client = Client(101, "Alice")
    dish = Dish("Steak", 25.0)
    order = client.make_order("regular", [dish])
    assert isinstance(order, RegularOrder)
    assert order.total_price() == 25.0

def test_client_id_and_name():
    client = Client(202, "Bob")
    assert client.client_id == 202
    assert client.name == "Bob"
