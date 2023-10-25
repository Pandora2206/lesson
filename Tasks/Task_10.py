from datetime import datetime, date,time
class Student:
    name = ""
    age = ""
    grade = ""
    b_day = False


    def __init__(self,
                 name,
                 age,
                 grade,
                 b_day):

        self.name = name
        self.age = age
        self.grade = grade
        self.b_day = b_day

    def display_info(self):
        """
        Имя: [имя],
        Возраст: [возраст],
        Класс: [класс]"
        :return:
        """
        print(f"Имя: [{self.name}]\n",
              f"Возраст: [{self.age}]\n",
              f"Класс: [{self.grade}]\n")

        return self.name, self.age, self.b_day, self.grade

    def congratulate(self, name, age,  b_day):
        if b_day:
            print(f"С днём рожденья {name}")
            print(f"Тебе сегодня {age+1}")


student_1 = Student("Alex", 12, 6, True)

student_2 = Student("Misha", 15, 9, False)

info = student_1.display_info()

student_2.congratulate(*info[0:3])
