from Customer import *
from Product import *
from ElectronicsStore import *

elStore = ElectronicsStore("Biba")

pomidor = Product("pomidor", price=100, quantity=10)
potato = Product("potato", price=50, quantity=100)
milk = Product("milk", price=1000, quantity=5)

elStore.add_product(pomidor)
elStore.add_product(potato)
elStore.add_product(milk)
# print(elStore.product_list)
elStore.display_products()