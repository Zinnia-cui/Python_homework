import pygame
import random

W = 800  # 窗口宽度
H = 600  # 窗口高度
ROW = 30  # 网格行数
COL = 40  # 网格列数

# 定义一个点类
class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def copy(self):
        return Point(row=self.row, col=self.col)

# 初始化游戏
def init_game():
    pygame.init()
    size = (W, H)  # 窗口大小，800x600 像素
    screen = pygame.display.set_mode(size)  # 创建窗口
    pygame.display.set_caption("贪吃蛇")  # 设置窗口标题
    return screen

# 绘制矩形
def draw_rect(screen, point, color):
    cell_width = W / COL
    cell_height = H / ROW
    left = point.col * cell_width
    top = point.row * cell_height
    pygame.draw.rect(screen, color, (left, top, cell_width, cell_height))

# 移动蛇
def move_snake(head, direction):
    if direction == 'left':
        head.col -= 1
    elif direction == 'right':
        head.col += 1
    elif direction == 'up':
        head.row -= 1
    elif direction == 'down':
        head.row += 1
    return head

# 控制蛇的方向
def control_snake(direct, event):
    if event.key in [ pygame.K_UP,pygame.K_w]:
        if direct in ['left', 'right']:
            direct = 'up'
    elif event.key in [pygame.K_DOWN ,pygame.K_s]:
        if direct in ['left', 'right']:
            direct = 'down'
    elif event.key in [pygame.K_LEFT,pygame.K_a]:
        if direct in ['up', 'down']:
            direct = 'left'
    elif event.key in [ pygame.K_RIGHT,pygame.K_d]:
        if direct in ['up', 'down']:
            direct = 'right'
    return direct

# 检测碰撞
def check_collision(head, snakes):
    if head.row < 0 or head.row >= 30 or head.col < 0 or head.col >= 40:
        return True
    for snake in snakes[1:]:
        if snake.row == head.row and snake.col == head.col:
            return True
    return False

# 食物生成函数
def gen_food(snakes, head):
    while True:
        pos = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))
        if not (head.row == pos.row and head.col == pos.col) and pos not in snakes:
            return pos

# 处理游戏结束后的显示
def game_over_screen(screen, score):
    bg_color = (255, 255, 255)  # 背景颜色 白色
    font_color = (0, 0, 0)  # 文字颜色 黑色
    screen.fill(bg_color)

    font = pygame.font.SysFont(None, 55)  # 创建字体对象
    game_over_text = font.render('Game Over!', True, font_color)
    score_text = font.render(f'Score: {score}', True, font_color)

    # 获取文本矩形并居中
    game_over_rect = game_over_text.get_rect(center=(400, 300 - 30))  # 游戏结束文本居中
    score_rect = score_text.get_rect(center=(400, 300 + 30))          # 得分文本居中
    # 绘制文本
    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    pygame.display.flip()
    pygame.time.delay(2000)  # 等待2秒以便玩家查看结果

# 主游戏循环
def main():
    screen = init_game()

    # 初始化变量
    head = Point(row=int(ROW / 2), col=int(COL / 2))  # 蛇头坐标
    # 蛇身坐标，初始长度为3
    snakes = [
        Point(row=head.row, col=head.col + 1),
        Point(row=head.row, col=head.col + 2),
        Point(row=head.row, col=head.col + 3)
    ]
    direction = 'left' # 初始方向为左
    food = gen_food(snakes, head) # 食物坐标
    score = 0 # 得分

    clock = pygame.time.Clock() # 控制帧率
    quit_game = True # 游戏退出标志

    while quit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = False #处理用户输入事件，如果用户点击关闭窗口则退出游戏
            elif event.type == pygame.KEYDOWN:
                direction = control_snake(direction, event) #如果按下方向键，则调用control_snake()更改蛇的移动方向。


        # 移动蛇
        head = move_snake(head.copy(), direction)

        # 检测是否吃到食物
        if head.row == food.row and head.col == food.col:
            score += 10
            food = gen_food(snakes, head)
        else:
            snakes.pop()#检测蛇头是否碰到食物。如果碰到，则增加得分并生成新的食物。如果没有，则移除蛇尾。

        #将更新后的蛇头加入到蛇身列表的最前面。
        snakes.insert(0, head)

        # 检测碰撞
        if check_collision(head, snakes):
            print("Game Over!")
            print("Score:", score)
            game_over_screen(screen, score)
            quit_game = False  # 退出游戏

        # 渲染
        screen.fill((255, 255, 255))  # 背景颜色 白色
        draw_rect(screen, head, (0, 128, 128))  # 蛇头颜色 蓝色
        draw_rect(screen, food, (255, 200, 0))  # 食物颜色 黄色
        for snake in snakes[1:]:
            draw_rect(screen, snake, (180, 180, 180))  # 蛇身颜色 灰色

        pygame.display.flip() # 更新屏幕
        clock.tick(20)  # 控制帧率

    # 退出游戏
    pygame.quit()

if __name__ == "__main__":
    main()
