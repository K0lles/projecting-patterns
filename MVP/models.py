class Model:

    _id = 1
    object_list = []

    def __init__(self, name, surname, age):
        self.id = Model._id
        self.name = name
        self.surname = surname
        self.age = age
        Model.object_list.append(self)
        Model._id += 1

    def __str__(self):
        return f"'{self.id}, {self.surname} {self.name}, {self.age} years old'"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def add_person(name, surname, age):
        if isinstance(surname, str) and isinstance(name, str):
            return Model(name, surname, age), True
        return None, False

    @staticmethod
    def get_all():
        if Model.object_list:
            return Model.object_list
        return None
