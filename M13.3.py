results = []
# 读取文件
with open('jisuan.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 计算结果并输出到文件
    with open('jieguo.txt', 'w', encoding='utf-8') as of:
        for line in lines:
            i = line.strip()
            if '+' in i:
                n1, n2 = i.split('+')
            elif '-' in i:
                n1, n2 = i.split('-')
            else:
                print('输入格式错误')
                continue  # 使用 continue 跳过当前行

            try:
                result = float(n1) + float(n2) if '+' in i else float(n1) - float(n2)
                results.append(result)
                s = "{:.2f}\n".format(result)
                of.write(s)  # 将结果写入文件
            except ValueError:
                print('数值转换错误:', i)  # 输出数值转换错误

