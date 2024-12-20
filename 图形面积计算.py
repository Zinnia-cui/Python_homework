import math
class Triangle:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        area=math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return area

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        area = math.pi * self.r ** 2
        return area

def main():
    a,b,c=eval(input())
    s1 = Circle(a/2)
    s2 = Circle(b/2)
    s3 = Circle(c/2)
    s0 = Triangle(a,b,c)

    s = 0.5*(s1.area()) + 0.5*(s2.area()) + 0.5*(s3.area()) + s0.area()
    print(f'{s:.2f}')

main()