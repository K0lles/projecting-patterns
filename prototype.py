from copy import deepcopy, copy
from abc import ABC, abstractmethod


class Engine:
    def __init__(self, cylinder_size, cylinder_amount, horses_power):
        self.cylinder_size = cylinder_size
        self.cylinder_amount = cylinder_amount
        self.horses_power = horses_power

    def __str__(self):
        return f"V{self.cylinder_size}, {self.horses_power} horses power"


class Car(ABC):
    @abstractmethod
    def ride(self):
        pass


class Audi(Car):
    def __init__(self, version, engine: Engine, sits_amount):
        self.version = version
        self.engine = engine
        self.sits_amount = sits_amount
        self.race = 0

    def ride(self):
        self.race += 10000

    def __str__(self):
        return f"Audi {self.version} with {self.engine} and has {self.sits_amount} of sits"


if __name__ == "__main__":
    audi_rs7 = Audi("RS7", Engine(3.5, 4, 244), 5)
    audi_r8 = deepcopy(audi_rs7)
    # audi_r8 = copy(audi_rs7)
    audi_r8.version = "R8"
    audi_r8.engine.cylinder_size = 5.0
    print(audi_rs7)
    print(audi_r8)
