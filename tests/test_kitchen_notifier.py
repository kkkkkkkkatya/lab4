from src.kitchen_notifier import KitchenNotifier, OrderNotifier
from src.menu import Dish
from src.order import OrderFactory


def test_observer_gets_notified(capfd):
    notifier = OrderNotifier()
    kitchen = KitchenNotifier()
    notifier.attach(kitchen)

    dish = Dish("Fish", 18.0)
    order = OrderFactory.create_order("regular", [dish])
    notifier.notify(order)

    out, _ = capfd.readouterr()
    assert "[Kitchen] New order received" in out


def test_observer_detach(capfd):
    notifier = OrderNotifier()
    kitchen = KitchenNotifier()
    notifier.attach(kitchen)
    notifier.detach(kitchen)

    dish = Dish("Pasta", 10.0)
    order = OrderFactory.create_order("regular", [dish])
    notifier.notify(order)

    out, _ = capfd.readouterr()
    assert out.strip() == ""
