# 编写程序实现删除字符串s中的两端空格和子字符串c的功能。
# 说明：不考虑去掉子字符串c后形成的新的子字符串。
# 例如：字符串s为“ abca bcd ”，子串c为bc，则调用该函数后，结果字符串s为“aa d"
s1=input()
s2=input()
s3=s1.replace(s2, '')
print(s3)

