class Person:

    _id = 1
    _all_persons = []

    def __init__(self, first_name: str, second_name: str, age: int):
        self.id = Person._id
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        Person._id += 1
        Person._all_persons.append(self)

    @staticmethod
    def get(pk: int):
        for person in Person._all_persons:
            if person.id == pk:
                return person

        return None

    @staticmethod
    def save(first_name: str, last_name: str, age: int):
        return Person(first_name, last_name, age)

    @staticmethod
    def delete(pk: int):
        for person in Person._all_persons:
            if person.id == pk:
                Person._all_persons.remove(person)
                return "success"

        return None

    @staticmethod
    def all():
        return Person._all_persons
