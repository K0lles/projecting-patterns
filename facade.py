class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Stock:
    __products = []

    @staticmethod
    def add_product_to_stock(product: Product):
        if product not in Stock.__products:
            Stock.__products.append(product)

    @staticmethod
    def remove_product_from_stock(product: Product):
        try:
            Stock.__products.remove(product)
        except ValueError:
            print(f"There is no {product.name} in stock yet")

    @staticmethod
    def get_products_from_stock():
        return Stock.__products


class ManagerOfStock:

    @staticmethod
    def find_product_on_stock(name: str):
        for product in Stock.get_products_from_stock():
            if product.name == name:
                return product


class BankBill:
    __bill = 100

    @staticmethod
    def pay(product: Product):
        BankBill.__bill += product.price - product.price * 0.04


class Administrator:

    @staticmethod
    def accept_call():
        print("Good morning, how can i help you?")

    @staticmethod
    def __ask_for_product(name: str):
        return ManagerOfStock.find_product_on_stock(name)

    @staticmethod
    def send_product_to_customer(name: str):
        product = Administrator.__ask_for_product(name)
        if product:
            BankBill.pay(product)
            return product
        print("This product is not in stock :(")


class Customer:

    def __init__(self, name, *args: str):
        self.name = name
        self.desired_product = list(args)

    def add_to_desired_products(self, *args):
        self.desired_product.extend(args)

    def order_products(self):
        ordered_products = []
        Administrator.accept_call()
        for product in self.desired_product:
            sent_product = Administrator.send_product_to_customer(product)
            if sent_product:
                ordered_products.append(sent_product)

        for product in ordered_products:
            self.desired_product.remove(product.name)

        return ordered_products


if __name__ == '__main__':
    screwdriver = Product("screwdriver", 14.99)
    nail = Product("nail", 0.99)
    Stock.add_product_to_stock(screwdriver)
    Stock.add_product_to_stock(nail)
    customer_one = Customer("Marina", "screwdriver", "nail", "tape")
    products = customer_one.order_products()
    print(products)
