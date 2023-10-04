import math
class Figure:
    def calculate_P(self):
        pass
    def calculate_S(self):
        pass

class Rectangle(Figure):
    line_1=0
    line_2=0
    def calculate_P(self):
        return self.line_1*2+self.line_2*2
    def calculate_S(self):
        return self.line_1*self.line_2
    def __init__(self,line_1,line_2):
        self.line_1=line_1
        self.line_2=line_2
        self.P=self.calculate_P()
        self.S=self.calculate_S()
class Circle(Figure) :
    r=0
    def calculate_P(self):
        return self.r*2*math.pi
        pass
    def calculate_S(self):
        return self.r*self.r*math.pi
        pass
    def __init__(self,r):
        self.r=r
        self.P=self.calculate_P()
        self.S=self.calculate_S()
rect=Rectangle(10,5)
print(rect.P,rect.S)
circ=Circle(5)
print(circ.P,circ.S)


