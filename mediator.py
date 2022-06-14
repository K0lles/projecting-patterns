from abc import ABC, abstractmethod
from enum import Enum
from random import choice


class OrderType(Enum):
    FOOD = 0
    DRINK = 1
    DESERT = 2


class Order:
    id = 1

    def __init__(self, order_type: OrderType):
        self.id = Order.id
        self.order_type = order_type
        Order.id += 1

    def __str__(self):
        return f"{self.id} {self.order_type.name}"


class WorkerType(Enum):
    WAITER = 0
    CHIEF = 1
    BARMAN = 2


class Action(Enum):
    GET_ORDER = 0
    FINISH_ORDER = 1


class IMediator(ABC):

    @abstractmethod
    def add_worker(self, worker):
        pass

    @abstractmethod
    def execute(self, order: Order, action: Action):
        pass


class IWorker(ABC):

    def __init__(self, name: str, mediator: IMediator):
        self.name = name
        self.orders = []
        self.mediator = IMediator
        mediator.add_worker(self)

    @abstractmethod
    def take_order(self, order: Order):
        self.orders.append(order)
        print(f"{self.type()} {self.name} has accepted your {order} and is going to execute it")

    @abstractmethod
    def finish_order(self, order: Order):
        try:
            self.orders.remove(order)
            print(f"{self.type().name} {self.name} has done order {order}")
        except ValueError:
            print(f"Sorry, but {self.type()} {self.name} do not have {order}")

    @abstractmethod
    def type(self) -> WorkerType:
        pass


class Waiter(IWorker):

    def __init__(self, name, mediator: IMediator):
        super().__init__(name, mediator)

    def take_order(self, order: Order):
        super().take_order(order)

    def finish_order(self, order: Order):
        super().finish_order(order)

    def type(self):
        return WorkerType.WAITER


class Barman(IWorker):

    def __init__(self, name, mediator: IMediator):
        super().__init__(name, mediator)

    def take_order(self, order: Order):
        super().take_order(order)

    def finish_order(self, order: Order):
        super().finish_order(order)

    def type(self):
        return WorkerType.BARMAN


class RestaurantMediator(IMediator):

    def __init__(self):
        self.workers = {WorkerType.WAITER: [],
                        WorkerType.BARMAN: []}

    def add_worker(self, worker: IWorker):
        if worker not in self.workers[worker.type()]:
            self.workers[worker.type()].append(worker)

    def execute(self, order: Order, action: Action):
        if action is Action.GET_ORDER:
            if order.order_type is OrderType.FOOD:
                choice(self.workers[WorkerType.WAITER]).take_order(order)
            else:
                choice(self.workers[WorkerType.BARMAN]).take_order(order)
        else:
            if order.order_type is OrderType.FOOD:
                choice(self.workers[WorkerType.WAITER]).finish_order(order)
            else:
                choice(self.workers[WorkerType.BARMAN]).finish_order(order)


if __name__ == '__main__':
    restaurant = RestaurantMediator()
    waiter = Waiter("Kolya", restaurant)
    barman = Barman("Andrej", restaurant)
    food_first_order = Order(OrderType.FOOD)
    food_second_order = Order(OrderType.FOOD)
    drink_first_order = Order(OrderType.DRINK)
    drink_second_order = Order(OrderType.DRINK)
    restaurant.execute(food_first_order, Action.GET_ORDER)
    restaurant.execute(food_second_order, Action.GET_ORDER)
    restaurant.execute(drink_first_order, Action.GET_ORDER)
    restaurant.execute(drink_second_order, Action.GET_ORDER)
    restaurant.execute(food_first_order, Action.FINISH_ORDER)
    restaurant.execute(food_second_order, Action.FINISH_ORDER)
    restaurant.execute(drink_first_order, Action.FINISH_ORDER)
    restaurant.execute(drink_second_order, Action.FINISH_ORDER)
