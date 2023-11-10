from Product import *


class ElectronicsStore:
    store_name: str = ""
    product_list: list[Product] = []

    def add_product(self, product: Product):
        self.product_list.append(product)

    def check_product(self, name: str, quantity: int):
        for product in self.product_list:
            if (product.name == name and
                    product.quantity >= quantity):
                return True
            else:
                return False

    def get_product(self, name: str, quantity: int, balance: float):
        if self.check_product(name, quantity):
            for product in self.product_list:
                if product.name == name:
                    if balance > quantity * product.price:
                        product.quantity -= quantity
                        return Product(getattr(product, 'name'),
                                       getattr(product, 'price'),
                                       quantity), quantity * product.price

        else:
            return

    def display_products(self):
        """
        получить каждый продукт из списка
        вывести всю информацию о нем наименование, цена, количество
        :return:
        """
        if len(self.product_list) == 0:
            return

        for product in self.product_list:
            product.display_info()

    def __init__(self, name: str):
        self.store_name = name
