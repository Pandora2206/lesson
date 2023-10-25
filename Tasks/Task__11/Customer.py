from ElectronicsStore import *
from Product import *
class `Customer:
    name: str
    balance: float
    list_product:str

    def make_purchase(self, store: ElectronicsStore,
                      product_name: str,
                      quantity: int):

        if store.check_product(product_name, quantity):
            if quantity > 0:
                for quantity in Product:
                quantity-
        else:
            return

            pass
            """
            написать функцию, которая возвращает продукт в нужном кол-во
            а в магазине убирает тоже кол-во 
            
            in store before:
             Product("pomidor", price=100, quantity=10)
             we buy  7:
             Product("pomidor", price=100, quantity=3)
             for customer 
             Product("pomidor", price=100, quantity=7)
            """



