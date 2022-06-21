import models


def creating_person(first_name: str, last_name: str, age: int):
    return models.Person.save(first_name, last_name, age)


def deleting_person(pk: int):
    return models.Person.delete(pk)


def show_all_persons():
    return models.Person.all()


def get_person(pk: int):
    return models.Person.get(pk)
