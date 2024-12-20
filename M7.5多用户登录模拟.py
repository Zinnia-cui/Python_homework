d = {"Kate": "666666", "tom": "123", "Jack": "123"}
count = 0  # 统一的错误计数器
flag = 0
for i in range(3):
    name = input("input username:")
    password = input("input password:")
    if name in d:
        if password == d.get(name):
            print('Success!')
            flag = 1
            break
if flag == 0:
    print("The user name or password is incorrect for 3 times!")



