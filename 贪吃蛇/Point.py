class Point:  #定义一个点类
    row=0
    col=0
    def __init__(self,row,col):
        self.row=row
        self.col=col

    def copy(self):
        return Point(row=self.row,col=self.col)