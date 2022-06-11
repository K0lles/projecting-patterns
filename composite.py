from abc import ABC, abstractmethod


class IItem(ABC):

    @abstractmethod
    def cost(self):
        pass


class Item(IItem):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def cost(self):
        return self.price


class Box(IItem):

    def __init__(self, name):
        self.name = name
        self.items = []

    def cost(self):
        total_price = 0
        for item in self.items:
            total_price += item.cost()
        return total_price

    def add_item(self, *args):
        self.items.extend(args)

    def remove_item(self, *args):
        for item in args:
            self.items.remove(item)


if __name__ == '__main__':
    box = Box("Box")
    box_small = Box("Smaller box")
    box_smallest = Box("The smallest box")
    nail = Item("Nail", 0.99)
    screw = Item("Screw", 1.49)
    tape = Item("Tape", 2.99)
    screwdriver = Item("Screwdriver", 12.99)
    box_smallest.add_item(screw, screw, screw, nail, nail)
    box_small.add_item(tape, tape, box_smallest)
    box.add_item(screwdriver, box_small, box_smallest, box_smallest)
    print(box_smallest.cost())
    print(box_small.cost())
    print(box.cost())
