import pygame
import random

# 定义一个点类
class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def copy(self):
        return Point(row=self.row, col=self.col)

# 初始化
pygame.init()
W = 800  # 窗口宽度
H = 600  # 窗口高度

ROW = 30  # 网格行数
COL = 40  # 网格列数

size = (W, H)  # 窗口大小
screen = pygame.display.set_mode(size)  # 创建窗口
pygame.display.set_caption("贪吃蛇")  # 设置窗口标题
head = Point(row=int(ROW / 2), col=int(COL / 2))  # 蛇头坐标

# 定义颜色
bg_color = (255, 255, 255)  # 背景颜色 白色
head_color = (0, 128, 128)  # 蛇头颜色 青色
food_color = (255, 255, 0)  # 食物颜色 黄色
snake_color = (200, 200, 200)  # 蛇颜色 灰色
font_color = (0, 0, 0)  # 文字颜色 黑色

# 定义蛇
snakes = [
    Point(row=head.row, col=head.col + 1),
    Point(row=head.row, col=head.col + 2),
    Point(row=head.row, col=head.col + 3)
]

# 定义方向
direct = 'left'  # 初始方向 left, right, up, down

# 绘制矩形
def rect(point, color):
    cell_width = W / COL
    cell_height = H / ROW
    left = point.col * cell_width
    top = point.row * cell_height

    pygame.draw.rect(screen, color, (left, top, cell_width, cell_height))

# 移动蛇
def move_snake(direct):
    global head
    if direct == 'left':
        head.col -= 1
    elif direct == 'right':
        head.col += 1
    elif direct == 'up':
        head.row -= 1
    elif direct == 'down':
        head.row += 1

# 控制蛇的方向
def control_snake(direct, event):
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        if direct == 'left' or direct == 'right':
            direct = 'up'
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        if direct == 'left' or direct == 'right':
            direct = 'down'
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        if direct == 'up' or direct == 'down':
            direct = 'left'
    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        if direct == 'up' or direct == 'down':
            direct = 'right'
    return direct

# 检测碰撞
def check_collision():
    if head.row < 0 or head.row >= ROW or head.col < 0 or head.col >= COL:
        return True
    for snake in snakes[1:]:
        if snake.row == head.row and snake.col == head.col:
            return True
    return False

# 食物生成函数
def gen_food():
    while True:
        pos = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))
        is_coll = head.row == pos.row and head.col == pos.col
        for snake in snakes:
            if snake.row == pos.row and snake.col == pos.col:
                is_coll = True
                break
        if not is_coll:
            return pos

# 生成食物
food = gen_food()
# 得分
score = 0

# 游戏循环
quit = True
clock = pygame.time.Clock()
while quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
        elif event.type == pygame.KEYDOWN:
            direct = control_snake(direct, event)

    eat = (head.row == food.row and head.col == food.col)
    if eat:
        score += 10
        food = gen_food()

    snakes.insert(0, head.copy()) #
    if not eat:
        snakes.pop()

    move_snake(direct)

    if check_collision():
        print("Game Over!")
        print("Score:", score)
        quit = False  # 退出游戏

    # 渲染
    screen.fill(bg_color)
    rect(head, head_color)
    rect(food, food_color)
    for snake in snakes:
        rect(snake, snake_color)

    pygame.display.flip()
    clock.tick(20)

# 游戏结束后的处理
font = pygame.font.SysFont(None, 55) #创建字体对象
game_over_text = font.render('Game Over!', True, font_color)
score_text = font.render(f'Score: {score}', True, font_color)

# 显示游戏结束信息

screen.fill(bg_color)
# 获取文本矩形并居中
game_over_rect = game_over_text.get_rect(center=(W // 2, H // 2 - 30))  # 游戏结束文本居中
score_rect = score_text.get_rect(center=(W // 2, H // 2 + 30))          # 得分文本居中
# 绘制文本
screen.blit(game_over_text, game_over_rect.topleft)
screen.blit(score_text, score_rect.topleft)
pygame.display.flip()



# 等待用户关闭窗口
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

pygame.quit()
