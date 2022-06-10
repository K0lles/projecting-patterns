from enum import Enum


class PizzaType(Enum):
    FOUR_CHEESES = 0,
    MARGARITA = 1,
    CLASSIC = 2


class Pizza:

    def __init__(self, price: float):
        self.__price = price

    def get_price(self):
        return self.__price


class PizzaFourCheeses(Pizza):
    def __init__(self):
        super().__init__(165.0)


class PizzaMargarita(Pizza):
    def __init__(self):
        super().__init__(90.0)


class PizzaClassic(Pizza):
    def __init__(self):
        super().__init__(125.0)


class PizzaFactory:

    @staticmethod
    def create_pizza(pizza_type: PizzaType) -> Pizza:
        pizza_dict = {
            PizzaType.FOUR_CHEESES: PizzaFourCheeses,
            PizzaType.MARGARITA: PizzaMargarita,
            PizzaType.CLASSIC: PizzaClassic
        }

        return pizza_dict[pizza_type]()


if __name__ == "__main__":
    for pizza in PizzaType:
        new_pizza = PizzaFactory.create_pizza(pizza)
        print(f'Pizza is {pizza} and its price is {new_pizza.get_price()}')
