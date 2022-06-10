from abc import ABC, abstractmethod
from enum import Enum


class PizzaDoughType(Enum):
    WHEAT = 0
    CORN = 1


class PizzaMeat(Enum):
    SALAMI = 0
    BACON = 1
    HAM = 2


class PizzaCheese(Enum):
    MOZZARELLA = 0
    DUTCH = 1
    PARMESAN = 2


class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.meat = []
        self.cheese = []

    def __str__(self):
        return f"Pizza {self.name} with {[meat for meat in self.meat]} and {self.cheese} prepared on {self.dough} dough"


class AbstractBuilder(ABC):
    @abstractmethod
    def set_dough(self) -> None:
        pass

    @abstractmethod
    def add_meat(self) -> None:
        pass

    @abstractmethod
    def add_cheese(self) -> None:
        pass

    @abstractmethod
    def get_pizza(self) -> Pizza:
        pass


class MargaritaBuilder(AbstractBuilder):
    def __init__(self):
        self.pizza = Pizza("Margarita")

    def set_dough(self) -> None:
        self.pizza.dough = PizzaDoughType.WHEAT

    def add_meat(self) -> None:
        self.pizza.meat.append(PizzaMeat.HAM)

    def add_cheese(self) -> None:
        self.pizza.cheese.extend([cheese for cheese in PizzaCheese])

    def get_pizza(self) -> Pizza:
        return self.pizza


class Director:
    def __init__(self, builder: AbstractBuilder):
        self.builder = builder

    def make_pizza(self):
        self.builder.set_dough()
        self.builder.add_meat()
        self.builder.add_cheese()

        return self.builder.get_pizza()


if __name__ == "__main__":
    builder_one = MargaritaBuilder()
    director = Director(builder_one)
    pizza = director.make_pizza()
    print(pizza)
