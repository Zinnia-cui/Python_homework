# 导入模块
import random


# 游戏状态变量
game_over = False
score = 0

# 蛇的结构
class SnakeSegment:
    def __init__(self, row, col):
        self.row = row
        self.col = col

# 全局变量
head = SnakeSegment(*initial_position)
snakes = []  # 蛇身列表
food_row, food_col = random.randint(0, ROW-1), random.randint(0, COL-1)  # 食物位置

# 函数定义
def handle_game_over():
    global game_over
    game_over = True
    print(f"游戏结束！你的得分是: {score}")
    print("重新开始吗？按'Y'继续，按'N'退出。")

def increase_score(points):
    global score
    score += points
    print(f"当前得分: {score}")

def reset_game():
    global head, snakes, score, game_over, food_row, food_col
    head = SnakeSegment(*initial_position)  # 重置蛇头位置
    snakes.clear()  # 清空蛇身
    score = 0  # 重置得分
    game_over = False  # 重置游戏状态
    place_food()  # 重新放置食物

def place_food():
    global food_row, food_col
    food_row, food_col = random.randint(0, ROW-1), random.randint(0, COL-1)  # 随机生成食物位置

def check_collision():
    if head.row < 0 or head.row >= ROW or head.col < 0 or head.col >= COL:
        return True  # 撞墙
    for segment in snakes:
        if segment.row == head.row and segment.col == head.col:
            return True  # 撞到自己
    return False

def move_snake(direction):
    if direction == 'left':
        head.col -= 1
    elif direction == 'right':
        head.col += 1
    elif direction == 'up':
        head.row -= 1
    elif direction == 'down':
        head.row += 1

def check_food():
    if head.row == food_row and head.col == food_col:
        increase_score(10)  # 吃到食物增加10分
        # 可根据实现增加蛇身
        snakes.append(SnakeSegment(head.row, head.col))  # 这里简单地在蛇身中增加一个新段
        place_food()  # 吃到食物后重新放置食物

# 游戏主循环
def game_loop():
    global game_over
    while True:
        if game_over:
            user_input = input()  # 等待用户输入
            if user_input.lower() == 'y':
                reset_game()
                continue
            else:
                break  # 退出游戏

        # 假设获得玩家的方向输入
        direction = input("输入移动方向 (left/right/up/down): ").strip().lower()
        move_snake(direction)  # 移动蛇
        if check_collision():  # 检测死亡
            handle_game_over()  # 处理死亡逻辑
            continue

        check_food()  # 检查是否吃到食物

        # 更新蛇身逻辑...

# 启动游戏
if __name__ == "__main__":
    reset_game()  # 初始化游戏
    game_loop()  # 启动游戏循环
