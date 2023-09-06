# ООП 

# Питца -> утка, курица, сокол
# Машина -> ВАЗ2103, Мерин, Буханка 
# WOW (персонажи NPC) -> Эльфы, люди, орки 
# map 
# Паттерн - шаблон 
# NPC
# Поля - класса 
# { 
#   -Name
#   -Age
#   -Gender 
#   -Class
#   -Weapon 
# }
# Методы - класса
# { 
#   - run
#   - talk
#   - fight
#   - wait 
# }

# class NameClass():
#   pass 

# Родительский 

# Global
a = 'slow run'
b = "wait"

def run():

    # local 
    a = "fast run" 
    print(a)







# Парадигмы программирования 
#  Функциональныый 
#  ООП 
#  goTo

# Концепции 
# 1. Наследование 
# 2. Инкапсуляция 
# 3. Полиморфизм 
# * Ассоциация 

# WOW (персонажи NPC) -> Эльфы, люди, орки

# Родительский класс 
class NPC:
    # свойство класса 
    Name = ""
    Age = ""
    Gender =""
    Class = ""


    # методы класса 
    def run(self):
        print("class_run")


    # поля класса 
    def __init__(self) -> None:
        self.run()
        run() 



# Экземпляр класс 
npc = NPC()


print(npc.Age)

