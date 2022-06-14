from abc import ABC, abstractmethod
from enum import Enum
from random import choice


class OrderType(Enum):
    MARGARITA = 1
    FOUR_CHEESES = 2
    BORSCH = 3


class Order:

    _id = 1

    def __init__(self, order_type: OrderType):
        self.id = Order._id
        self.order_type = order_type
        Order._id += 1

    def __str__(self):
        return f"#{self.id}"


class Observer(ABC):

    @abstractmethod
    def update(self):
        pass


class Worker(ABC):

    def __init__(self):
        self.observer_list = []

    @abstractmethod
    def take_order(self, order: Order):
        pass

    def add_observer(self, observer: Observer):
        if observer not in self.observer_list:
            self.observer_list.append(observer)

    def delete_observer(self, observer: Observer):
        try:
            self.observer_list.remove(observer)
        except ValueError:
            print(f"There is no such observer as {observer}")

    @abstractmethod
    def get_order(self):
        pass

    def notify(self, order_id: int):
        for observer in self.observer_list:
            observer.update(order_id)


class Chief(Worker):

    def __init__(self):
        super().__init__()
        self.order_list = []
        self.finished_orders = []

    def take_order(self, order: Order):
        self.order_list.append(order)

    def making_order(self):
        if not self.order_list:
            return

        current_order = choice(self.order_list)
        print(f"Now i`m processing order {current_order}")
        self.order_list.remove(current_order)
        self.finished_orders.append(current_order)
        self.notify(current_order.id)

    def get_order(self, order_id: int):
        order_to_delete = None
        for order in self.finished_orders:
            if order.id == order_id:
                order_to_delete = order
                break
        self.finished_orders.remove(order_to_delete)


class Customer(Observer):

    def __init__(self, name, chief: Worker):
        self.name = name
        self.chief = chief
        self.order = None

    def update(self, order_id: int):
        if self.order.id == order_id:
            self.chief.get_order(self.order.id)
            print(f"{self.name} has got his order and is glad!")
            self.chief.delete_observer(self)

    def add_order(self, order: Order):
        self.order = order
        self.chief.take_order(order)
        self.chief.add_observer(self)


if __name__ == '__main__':
    chief = Chief()
    marina = Customer("Marina", chief)
    andrij = Customer("Andrij", chief)
    john = Customer("John", chief)

    marina.add_order(Order(OrderType.MARGARITA))
    andrij.add_order(Order(OrderType.FOUR_CHEESES))
    john.add_order(Order(OrderType.FOUR_CHEESES))

    chief.making_order()
    chief.making_order()
    chief.making_order()
