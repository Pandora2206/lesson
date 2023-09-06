import time

# PEP8 - стандарт форматирования кода
from abc import  ABC, abstractmethod, ABCMeta


class NPC(ABC):


    # свойство класса 
    Name = ""
    Age = ""
    Gender = ""
    Class = ""

    __TimeCreated = ""



    # методы класса 
    def run(self):
        print("run")

    @abstractmethod
    def eat(self):
        print("Om-om")

    def born(self):
        print("Введи характеристики:")
        self.Name = input("Кто ты воин?: ")
        self.Age = int(input("Возраст?: "))
        self.Gender = input("Пол?: ")
        self.Class = input("Роль?: ")

    def test_born(self):
        self.Name = "Name"
        self.Age = '10'
        self.Gender = "Male"
        self.Class = 'Warrior'

    def print_state(self):
        print("Ваши статы: ")
        print(self.Name)
        print(self.Age)
        print(self.Gender)
        print(self.Class)
        
    # поля класса 
    def __init__(self) -> None:
        self.test_born()
        self.__TimeCreated = time.ctime(time.time())
        print(self.__TimeCreated)