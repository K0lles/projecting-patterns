from abc import ABC, abstractmethod


class IAlgorithm(ABC):

    @abstractmethod
    def make_route(self, your_location, final_destination):
        pass


class Navigator:

    def __init__(self, current_location: str, algorithm: IAlgorithm):
        self.current_location = current_location
        self.algorithm = algorithm

    def find_route(self, destination: str):
        self.algorithm.make_route(self.current_location, destination)
        self.current_location = destination


class BicycleAlgorithm(IAlgorithm):

    def make_route(self, your_location, final_destination):
        print(f"Founded way for bicycle from {your_location} to {final_destination}")


class WalkAlgorithm(IAlgorithm):

    def make_route(self, your_location, final_destination):
        print(f"Founded way for walking from {your_location} to {final_destination}")


class CarAlgorithm(IAlgorithm):

    def make_route(self, your_location, final_destination):
        print(f"Founded way for car from {your_location} to {final_destination}")


if __name__ == '__main__':
    navigator = Navigator("airport", WalkAlgorithm())
    navigator.find_route("park")

    navigator.algorithm = BicycleAlgorithm()
    navigator.find_route("pizzeria")

    navigator.algorithm = CarAlgorithm()
    navigator.find_route("home")
