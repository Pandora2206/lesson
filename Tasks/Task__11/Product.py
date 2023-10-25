class Product:
    name = 0
    price = 0
    quantity = 0

    def display_nfo(self):
        print("++++++++++++++++++++++++")
        print(self.name)
        print(self.price)
        print(self.quantity)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

