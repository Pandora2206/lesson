class TriangleChecker:
    line_1 = 0    
    line_2 = 0    
    line_3 = 0 

    def __init__(self, line_1_input: object, line_2_input: object, line_3_input: object):
        if isinstance(line_1_input, (int, float)) and isinstance(line_1_input, (int, float)) and isinstance(line_1_input, (int, float)):
            self.line_1 = float(line_1_input)
            self.line_2 = float(line_2_input)
            self.line_3 = float(line_3_input)
        
    def is_triangle(self):
        if (self.line_1 > 0) and (self.line_2 > 0) and (self.line_3 > 0):
            
            if self.line_1 + self.line_2 > self.line_3 and self.line_1 + self.line_3 > self.line_2:
                print("Ура можно построить треугольник")
            else:
                print("Жаль, но из этого треугольник не сделать")
            
        else:
            print("Отрицательные числа!!!")


triangle = TriangleChecker(3, 2, 2)
triangle.is_triangle()
