class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"<Person>\n" \
               f"\t<name>{self.name}</name>\n" \
               f"\t<age>{self.age}</age>\n" \
               f"</Person>"


class Adapter(Person):
    def __init__(self, person: Person):
        self.person = person

    def get_info(self):
        string_to_return = "Person {" + "\n"
        string_to_return += f"\tname: '{self.person.name}',\n" \
                            f"\tage: {self.person.age}\n"
        string_to_return += "}"
        return string_to_return


if __name__ == '__main__':
    person_in_xml = Person("Alina", 19)
    person_in_json = Adapter(person_in_xml)
    print(person_in_xml.get_info())
    print(person_in_json.get_info())
