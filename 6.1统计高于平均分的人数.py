'''
【问题描述】从若干学生成绩中统计高于(严格的大于)平均分的人数，用-1做为学生成绩数据的结束标志。如果没有输入成绩，则输出0。
【输入形式】一组学生的成绩
【输出形式】高于平均分的学生人数
【样例输入】70 50 80 -1
【样例输出】2'''

# 输入以空格分隔的成绩
scores = input().split()
ls = [int(score) for score in scores]
for j in range(len(ls)):
    if int(ls[j]) == -1:
        break
if len(ls) == 1:# 如果没有有效成绩
    print(0)
else:
    avg = sum(ls)/(len(ls)-1)
    count = 0
    for i in ls:
        if i > avg: # 统计高于平均分的学生人数
            count += 1
    print(count)