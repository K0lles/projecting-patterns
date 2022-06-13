from abc import ABC, abstractmethod
from enum import Enum


class Action(Enum):
    QUESTION = 0
    MAKE_ORDER = 1


class Handler(ABC):

    def __init__(self, successor):
        self.__successor = successor

    @property
    def successor(self):
        return self.__successor

    @abstractmethod
    def serve(self, customer_need: Action):
        if not self._check_operation(customer_need):
            self.__successor.serve(customer_need)

    @abstractmethod
    def _check_operation(self, customer_need: Action):
        pass


class Administrator(Handler):
    
    def __init__(self, successor):
        self.__successor = successor

    def serve(self, customer_need: Action):
        print(f"Customer action {customer_need} is starting processing by Administrator")
        if self._check_operation(customer_need):
            print(f"Customer got the answer on his question")
        print(f"This operation cannot be executed by Administrator. Giving it to other participant")
        self.__successor.serve(customer_need)

    def _check_operation(self, action: Action):
        if action is Action.QUESTION:
            return True
        return False


class ManagerOfStock(Handler):

    def __init__(self, successor=None):
        self.__successor = successor

    def serve(self, customer_need: Action):
        print(f"Customer action {customer_need} is starting processing by Manager of Stock")
        print(f"Manager has made this order and in the nearest future it will be delivered")

    def _check_operation(self, customer_need: Action):
        if self.__successor:
            return True
        return False


if __name__ == '__main__':
    manager = ManagerOfStock()
    administrator = Administrator(manager)
    administrator.serve(Action.MAKE_ORDER)
