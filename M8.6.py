import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def setRadius(self, radius):
        if self.radius > 0:
            self.radius = radius
    def getRadius(self):
        return self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius

#创建圆对象r1,计算其圆周长并输出
radius1=float(input())
r1=Circle(radius1)
print("r1.radius={:<.1f},r1.perimeter={:<.1f}".format(r1.getRadius(),r1.perimeter()))
#获取输入值,调用成员方法setRadius修改圆对象r1的半径为原来值的2倍，并输出修改后的半径和周长
r1.setRadius(2*r1.getRadius())
print("r1.getRadius={:<.1f},r1.perimeter={:<.1f}".format(r1.getRadius(),r1.perimeter()))




