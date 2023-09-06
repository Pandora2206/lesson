class Soda:
    
    # аргумент 
    element = ""

    def __init__(self, element_input = None) -> None:
        if isinstance(element_input, str):
            self.element = element_input
        else:
            self.element = None 

    def show_my_drink(self):
        if self.element:
            print(f"Газировка с {self.element}")
        else:
            print("Обычная газировка")
