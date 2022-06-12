class Shared:
    def __init__(self, company: str, position: str):
        self.__company = company
        self.__position = position

    @property
    def company(self):
        return self.__company

    @property
    def position(self):
        return self.__position


class Unique:
    def __init__(self, name: str, passport: str):
        self.__name = name
        self.__passport = passport

    @property
    def name(self):
        return self.__name

    @property
    def passport(self):
        return self.__passport


class Flyweight:
    def __init__(self, shared: Shared):
        self.__shared = shared

    def process(self, unique: Unique):
        print(f"New data: common - {self.__shared.company}, {self.__shared.position};"
              f"unique - {unique.name}, {unique.passport}")

    def get_data(self):
        return f"{self.__shared.company}, {self.__shared.position}"


class FlyweightFactory:

    def get_key(self, shared):
        return f"{shared.company}, {shared.position}"

    def __init__(self, shared_list: list):
        self.__flyweights = {}
        for shared in shared_list:
            self.__flyweights[self.get_key(shared)] = Flyweight(shared)

    def get_flyweight(self, shared: Shared):
        key = self.get_key(shared)
        if not self.__flyweights.get(key):
            print(f"There is no such keys as '{shared.company}, {shared.position}'")
            self.__flyweights[key] = Flyweight(shared)
        return self.__flyweights[key]

    def list_flyweights(self):
        print(f"Amount: {len(self.__flyweights)}")
        for flyweight in self.__flyweights.values():
            print(flyweight.get_data())


def add_specialist_database(ff: FlyweightFactory,
                            name: str,
                            passport: str,
                            company: str,
                            position: str):
    flyweight = ff.get_flyweight(Shared(company, position))
    flyweight.process(Unique(name, passport))


if __name__ == '__main__':
    shared_list = [Shared("Google", "Senior"),
                   Shared("Yahoo", "Junior"),
                   Shared("Microsoft", "QA"),
                   Shared("Apple", 'Product manager')]
    factory = FlyweightFactory(shared_list)
    factory.list_flyweights()
    print("---------------")
    add_specialist_database(factory, "Banjo", "754687", "Google", "Senior")
    add_specialist_database(factory, "Maja", "875465", "Yahoo", "Junior")
    add_specialist_database(factory, "Linda", "756452", "Yahoo", "Junior")
    factory.list_flyweights()

