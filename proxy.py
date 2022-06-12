from abc import ABC, abstractmethod


class ISite(ABC):

    @abstractmethod
    def get_page(self, number: str):
        pass


class SimpleSite(ISite):

    def get_page(self, number: str):
        return f"This is page {number}"


class SiteProxy(ISite):

    def __init__(self, site: SimpleSite):
        self.__site = site
        self.__cache = {}

    def get_page(self, number: str):
        if not self.__cache.get(number):
            page = self.__site.get_page(number)
            self.__cache[number] = page
        else:
            page = self.__cache.get(number) + " returned from cache"
        return page


if __name__ == '__main__':
    proxy = SiteProxy(SimpleSite())

    print(proxy.get_page("home"))
    print(proxy.get_page("about"))
    print(proxy.get_page("about"))
    print(proxy.get_page("home"))
