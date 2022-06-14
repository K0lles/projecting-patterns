class PizzaMaker:

    def __init__(self):
        self.characteristics = []

    def make_pizza(self):
        print(f"Increasing temperature in oven")
        print(f"Putting your pizza into over!")
        print(f"Ready, {self.characteristics}")


class MargaritaMaker(PizzaMaker):

    def __init__(self):
        super().__init__()

    def add_dough(self):
        self.characteristics.append("thin")

    def add_sauce(self):
        self.characteristics.append("ketchup and taco")

    def add_topping(self):
        self.characteristics.extend(["cheese", "tomato"])


class FourCheesesMaker(PizzaMaker):

    def __init__(self):
        super().__init__()

    def add_dough(self):
        self.characteristics.append("thin")

    def add_sauce(self):
        self.characteristics.append("mayonnaise")

    def add_topping(self):
        self.characteristics.extend(["parmezan", "cheese", "mozzarella", "chedar"])


if __name__ == '__main__':
    pizza_one = MargaritaMaker()
    pizza_one.add_dough()
    pizza_one.add_sauce()
    pizza_one.add_topping()
    pizza_one.make_pizza()
    print("-" * 30)
    pizza_two = FourCheesesMaker()
    pizza_two.add_dough()
    pizza_two.add_sauce()
    pizza_two.add_topping()
    pizza_two.make_pizza()
