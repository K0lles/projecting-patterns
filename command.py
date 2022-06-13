from abc import ABC, abstractmethod


class ICommand(ABC):

    @abstractmethod
    def execute(self):
        pass


class Text:

    def save(self):
        print("Text is saved")

    def translate(self):
        print("Text is translated")


class Image:

    def zip(self):
        print("Image was zipped")

    def save(self):
        print("Image was saved")


class SaveTextCommand(ICommand):

    def __init__(self, text: Text):
        self.__text = (text)

    def execute(self):
        self.__text.save()


class TranslateTextCommand(ICommand):

    def __init__(self, text: Text):
        self.__text = text

    def execute(self):
        self.__text.translate()


class SaveImageCommand(ICommand):

    def __init__(self, image: Image):
        self.__image = image

    def execute(self):
        self.__image.save()


class ZipImageCommand(ICommand):

    def __init__(self, image: Image):
        self.__image = image

    def execute(self):
        self.__image.zip()


class Program:

    def __init__(self, *command_list):
        self.__command_list = list(command_list)

    def add_command(self, command: ICommand):
        self.__command_list.append(command)

    def execute_commands(self):
        for command in self.__command_list:
            command.execute()


if __name__ == '__main__':
    image_one = Image()
    text_one = Text()
    program = Program()
    program.add_command(SaveTextCommand(text_one))
    program.add_command((ZipImageCommand(image_one)))
    program.execute_commands()
