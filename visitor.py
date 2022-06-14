from abc import ABC, abstractmethod


class IVisitor(ABC):

    @abstractmethod
    def visit(self, place):
        pass


class IPlace(ABC):

    @abstractmethod
    def accept(self, visitor: IVisitor):
        pass


class CafePlace(IPlace):

    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class ParkPlace(IPlace):

    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class CinemaPlace(IPlace):

    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class HolidayMaker(IVisitor):

    def __init__(self):
        self.places = ""

    def visit(self, place: IPlace):
        if isinstance(place, CafePlace):
            self.places = "Was in Cafe"
        elif isinstance(place, ParkPlace):
            self.places = "Was in Park"
        elif isinstance(place, CinemaPlace):
            self.places = "Was in Cinema"


if __name__ == '__main__':
    visitor = HolidayMaker()
    cinema = CinemaPlace()
    park = ParkPlace()
    cafe = CafePlace()

    cafe.accept(visitor)
    print(visitor.places)

    park.accept(visitor)
    print(visitor.places)

    cinema.accept(visitor)
    print(visitor.places)
