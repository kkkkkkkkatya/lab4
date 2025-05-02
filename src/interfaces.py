from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, order):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, order):
        pass
