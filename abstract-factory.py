from abc import ABC, abstractmethod


class AbstractButton(ABC):
    """
    Abstract class for realisation Button element on different OS
    """
    def __init__(self, system):
        self._system = system

    @abstractmethod
    def create(self):
        pass


class AbstractCheckBox(ABC):
    """
    Abstract class for realisation Checkbox button of different OS
    """
    def __init__(self, system):
        self._system = system

    @abstractmethod
    def create(self):
        pass


class WinButton(AbstractButton):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print("Button element for Windows was created")


class WinCheckBox(AbstractCheckBox):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print("CheckBox element for Windows was created")


class MacButton(AbstractButton):
    def __init__(self):
        super().__init__("MacOS")

    def create(self):
        print("Button element for MacOS was created")


class MacCheckBox(AbstractCheckBox):
    def __init__(self):
        super().__init__("MacOS")

    def create(self):
        print("CheckBox element for MacOS was created")


class AbstractFactory(ABC):
    @abstractmethod
    def get_button(self):
        pass

    @abstractmethod
    def get_checkbox(self):
        pass


class WinFactory(AbstractFactory):
    def get_button(self):
        return WinButton()

    def get_checkbox(self):
        return WinCheckBox()


class MacFactory(AbstractFactory):
    def get_button(self):
        return MacButton()

    def get_checkbox(self):
        return MacCheckBox()


class Application:
    def __init__(self, factory: AbstractFactory):
        self.__factory = factory

    def get_checkbox(self):
        return self.__factory().get_checkbox().create()

    def get_button(self):
        return self.__factory().get_button().create()


if __name__ == "__main__":
    win = Application(WinFactory)
    win.get_checkbox()
    win.get_button()

    mac = Application(MacFactory)
    mac.get_checkbox()
    mac.get_button()
