class NPC:
    # свойство класса 
    Name = ""
    Age = ""
    Gender =""
    Class = ""

    # методы класса 
    def run(self):
        print("run")

    def eat(self):
        print("Om-om")

    def born(self):
        self.Name = input()
        self.Age = int(input())
        self.Gender = input()
        self.Class = input()

    def print_state(self):
        print(self.Name)
        print(self.Age)
        print(self.Gender)
        print(self.Class)
        
    # поля класса 
    def __init__(self) -> None:
        self.born()