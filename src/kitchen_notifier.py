from .interfaces import Observer, Subject


class KitchenNotifier(Observer):
    def update(self, order):
        print(f"[Kitchen] New order received: {order}")


class OrderNotifier(Subject):
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, order):
        for observer in self._observers:
            observer.update(order)
