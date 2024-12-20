# 生成食物
import pygame
import random
from Point import Point
ROW=30  #网格行数
COL=40  #网格列数
i=0  #计数器
snakes=[]  #蛇的坐标列表
head=Point(row=0,col=0)  #蛇头坐标
def gen_food():
    while 1:
        pos = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))

        #
        is_coll = False

        # 是否跟蛇碰上了
        if head.row == pos.row and head.col == pos.col:
            is_coll = True
            i+=1

        # 蛇身子
        for snake in snakes:
            if snake.row == pos.row and snake.col == pos.col:
                is_coll = True
                break

        if not is_coll:
            break

    return pos


food= gen_food()  #食物坐标