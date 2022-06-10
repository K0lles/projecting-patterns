from enum import Enum
#
#
# class PizzaType(Enum):
#     FOUR_CHEESES = 0,
#     MARGARITA = 1,
#     CLASSIC = 2
#
#
# class Pizza:
#     """
#     Basic class for creating different types of pizza
#     """
#     def __init__(self, price: float):
#         self.__price = price
#
#     def get_price(self):
#         return self.__price
#
#
# class PizzaFourCheeses(Pizza):
#     def __int__(self):
#         super().__init__(165.0)
#
#
# class PizzaMargarita(Pizza):
#     def __init__(self):
#         super().__init__(100.0)
#
#
# class PizzaClassic(Pizza):
#     def __init__(self):
#         super().__init__(120.0)
#
#
# class PizzaFactory:
#     """
#     Factory class
#     """
#
#     @staticmethod
#     def create_pizza(pizza_type: PizzaType):
#
#         factory_pizza_dict = {
#             PizzaType.FOUR_CHEESES: PizzaFourCheeses,
#             PizzaType.MARGARITA: PizzaMargarita,
#             PizzaType.CLASSIC: PizzaClassic
#         }
#
#         return factory_pizza_dict[pizza_type]()
#
#
# def create_pizza(pizza_type: PizzaType) -> Pizza:
#     factory_pizza_dict = {
#         PizzaType.FOUR_CHEESES: PizzaFourCheeses,
#         PizzaType.MARGARITA: PizzaMargarita,
#         PizzaType.CLASSIC: PizzaClassic
#     }
#     print(factory_pizza_dict[pizza_type])
#     return factory_pizza_dict[pizza_type]()
#
#
# if __name__ == '__main__':
#     for pizza in PizzaType:
#         print(pizza)
#         some_pizza = create_pizza(pizza)
#         print(some_pizza.get_price())


class PizzaType(Enum):
    """
    Перечисление текущих рецептов пицц в пиццерии,
    которые можно приготовить
    """
    MARGARITA = 0,
    MEXICO = 1,
    STELLA = 2


class Pizza:
    """
    Базовый класс для пицц, которые можно
    приготовить в пиццерии
    """
    def __init__(self, price: float):
        self.__price = price

    def get_price(self) -> float:
        return self.__price


class PizzaMargarita(Pizza):
    def __init__(self):
        super().__init__(3.5)


class PizzaMexico(Pizza):
    def __init__(self):
        super().__init__(17.5)


class PizzaStella(Pizza):
    def __init__(self):
        super().__init__(5.5)


def create_pizza(pizza_type: PizzaType) -> Pizza:
    """
    Factory Method
    """
    factory_dict = {
        PizzaType.MARGARITA: PizzaMargarita,
        PizzaType.MEXICO: PizzaMexico,
        PizzaType.STELLA: PizzaStella
    }
    return factory_dict[pizza_type]()


if __name__ == '__main__':
    for pizza in PizzaType:
        my_pizza = create_pizza(pizza)
        print(f'Pizza type: {pizza}, price: {my_pizza.get_price()}')