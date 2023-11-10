from ElectronicsStore import *
from Product import *


class Customer:
    name: str
    balance: float
    list_product: str

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_purchase(self,
                      store: ElectronicsStore,
                      product_name: str,
                      quantity: int = 1):
        if quantity == 0:
            return

        product, price = store.get_product(product_name, quantity, self.balance)
        self.balance -= price
        print(product.display_info())


