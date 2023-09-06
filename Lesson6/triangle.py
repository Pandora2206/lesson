class TriangleChecker:
    line_1 = None
    line_2 = None
    line_3 = None

    def __init__(self, line_1_input, line_2_input, line_3_input):
        if (isinstance(line_1_input, (int, float)) and 
            isinstance(line_2_input, (int, float)) and 
            isinstance(line_3_input, (int, float))):

            self.line_1 = line_1_input
            self.line_2 = line_2_input
            self.line_3 = line_3_input

        elif (isinstance(line_1_input, (str)) and 
              isinstance(line_2_input, (str)) and 
              isinstance(line_3_input, (str))): 
            try:
                self.line_1 = float(line_1_input)
                self.line_2 = float(line_2_input)
                self.line_3 = float(line_3_input)
            except:
                print("Вы ввели не числа!!!")

    def is_triangle(self):
        if self.line_1 +self.line_2 >self.line_3 and  self.line_1 + self.line_3 > self.line_2:
            print("Ура можно построить треугольник")
        else:print("Жаль, но из этого треугольник не сделать")

    def print_line(self):
        return self.line_1, self.line_2, self.line_3

a = input()
b = input()
c = input()
triangle=TriangleChecker(a, b, c)
triangle.is_triangle()
print(triangle.print_line())
