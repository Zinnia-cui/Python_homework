# 计算国王要向宰相奖励的麦粒数量
sum = 0
# 循环64个格子，计算每个格子的麦粒数量
for i in range(0,64):
    s = 2 ** i
    sum += s
print("{}".format(sum))  # 输出总麦粒数量
gram = sum * 50 / 1000
t = gram / 1000000# 克转为吨
print("{:.2f}t".format(t))  # 输出总麦粒的总重量
# 计算全部麦粒的体积
v = gram /500 * 550  # 体积
maili_v = v / 1000000  # 毫升转为立方米
# 计算麦粒在足球场上的高度
h = maili_v / 7140
print("{:.2f}m".format( h ))

