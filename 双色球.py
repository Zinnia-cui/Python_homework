def check_award(winning_red, winning_blue, user_red, user_blue):
    # 计算红球和蓝球的匹配情况
    red_matches = len(set(winning_red) & set(user_red))  # 红球匹配数量
    blue_matches = winning_blue == user_blue  # 蓝球是否匹配

    # 输出中奖号码
    print(f"The winning red ball is {{{', '.join(map(str, sorted(winning_red)))}}}")
    print(f"The winning blue ball is {winning_blue}")
    print(f"The red ball you selected is {{{', '.join(map(str, user_red))}}}")
    print(f"The blue ball you selected is {user_blue}")
    print(f"The blue ball you selected is {user_blue}")

    # 确定奖项
    if red_matches == 6 and blue_matches:
        return "the first award"
    elif red_matches == 6:
        return "the second award"
    elif red_matches == 5 and blue_matches:
        return "the third award"
    elif red_matches == 5 or (red_matches == 4 and blue_matches):
        return "the fourth award"
    elif red_matches == 4 or (red_matches == 3 and blue_matches):
        return "the fifth award"
    elif blue_matches:
        return "the sixth award"
    else:
        return "Ha ha, daydream, wake up!"

# 假设的中奖号码
winning_red = [2,14,31,25,18,27]
winning_blue = 15

# 用户输入蓝球号码
user_blue = int(input("Select 1 blue balls from 1-16: "))

# 用户输入红球号码
user_red = []
print("Select 6 red balls from 1-33: ")
for i in range(6):
    red_ball = int(input())
    user_red.append(red_ball)

# 输出结果
award = check_award(winning_red, winning_blue, user_red, user_blue)
print(award)

