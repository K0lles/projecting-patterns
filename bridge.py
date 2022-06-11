from time import sleep
from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):

    def __init__(self, name: str,  side_amount=0, side_length=0):
        self.name = name
        self.side_amount = side_amount
        self.side_length = side_length
        self.colour = "Neutral"

    @abstractmethod
    def get_square(self):
        return self.side_length * self.side_amount

    @abstractmethod
    def __str__(self):
        if self.side_amount:
            return f"{self.colour} {self.name} with {self.side_length} radius length"
        return f"{self.colour} {self.name} with {self.side_amount}, {self.side_length} each"


class Triangle(Figure):

    def __init__(self, side_length):
        super().__init__("triangle", 3, side_length)

    def get_square(self):
        return super().get_square()

    def __str__(self):
        return super().__str__()


class Round(Figure):

    def __init__(self, radius):
        super().__init__("round", side_length=radius)

    def get_square(self):
        return pi * (self.side_length ** 2)

    def __str__(self):
        return super().__str__()


class Colour:

    @abstractmethod
    def __init__(self, colour_name: str,
                 shade: str,
                 percent_of_shade: int,
                 saturation: int):
        self.colour_name = colour_name
        self.shade = shade
        self.percent_of_shade = percent_of_shade
        self.saturation = saturation

    def __str__(self):
        return f"{self.colour_name} with {self.percent_of_shade}% shade of {self.shade} " \
               f"and {self.saturation}% saturation"


class IColouringImplementor(ABC):

    def __init__(self, colour: Colour, implementor_type: str):
        self.colour = colour
        self.__implementor_type = implementor_type

    @abstractmethod
    def set_colour(self, figure: Figure):
        figure.colour = self.colour
        return figure

    @abstractmethod
    def get_colour(self):
        return self.colour

    @abstractmethod
    def get_implementor_type(self):
        return self.__implementor_type


class ManualColouringImplementor(IColouringImplementor):

    def __init__(self, colour: Colour):
        super().__init__(colour, "manual implementor")

    def set_colour(self, figure: Figure):
        sleep(1 * (figure.side_length + figure.side_amount))
        return super().set_colour(figure)

    def get_colour(self):
        return super().get_colour()

    def get_implementor_type(self):
        return super().get_implementor_type()


class AutoColouringImplementor(IColouringImplementor):

    def __init__(self, colour: Colour):
        super().__init__(colour, "automatic implementor")

    def set_colour(self, figure: Figure):
        sleep(0.5 * (figure.side_length + figure.side_amount))
        return super().set_colour(figure)

    def get_colour(self):
        return super().get_colour()

    def get_implementor_type(self):
        return super().get_implementor_type()


class Colouring:

    def __init__(self, implementor: IColouringImplementor):
        self.__implementor = implementor

    def colour_figure(self, figure: Figure):
        print(f"Starting colouring your {figure.name} by {self.__implementor.get_implementor_type()}")
        return self.__implementor.set_colour(figure)

    def get_colour(self):
        return self.__implementor.get_colour()


if __name__ == '__main__':
    triangle_one = Triangle(5)
    round_one = Round(4)
    red_colour = Colour("Red", "white", 34, 45)
    blue_colour = Colour("Blue", "black", 12, 28)
    implementor_one = AutoColouringImplementor(red_colour)
    implementor_second = ManualColouringImplementor(blue_colour)
    colouring_one = Colouring(implementor_one)
    colouring_second = Colouring(implementor_second)
    print(triangle_one)
    print(round_one)
    print(colouring_one.colour_figure(triangle_one))
    print(colouring_second.colour_figure(round_one))
