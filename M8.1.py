class Time():
    def __init__(self,h=0,m=0,s=0):
        self.hour = h
        self.minute = m
        self.second = s
    def setTime(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s
    def showTime(self):
        print("{:0>2}:{:0>2}:{:0>2}".format(self.hour,self.minute,self.second))

    #定义nextHour方法，采用24小时制,片段代码如下：
    def nextHour(self):
        if self.hour == 23:
            self.hour = 0
        else:
            self.hour += 1

def main():
    h, m, s = map(int,input().split())
    t = Time()
    t.setTime(h, m, s)
    t.nextHour()
    t.showTime()
main()


