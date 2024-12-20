class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def IsIsosceles(self):
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return True
        else:
            return False
    def getArea(self):
        s = (self.a + self.b + self.c) / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
