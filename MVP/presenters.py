import models


def add_person(name, surname, age):
    person, is_updated = models.Model.add_person(name, surname, int(age))

    if is_updated:
        return person
    else:
        return f"Nothing was updated"


def show_all_persons():
    return models.Model.object_list
