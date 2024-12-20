text = input()
dict = {}
for char in text:
    if char.isalpha():  # 只考虑字母
       dict[char] = dict.get(char, 0) + 1
       #get()方法返回指定键的值，如果键不存在，则返回默认值（这里是0）
       #dict[char] = text.count(char)  # 统计字母出现的次数
k = list(dict.keys())
n = 0
for j in k:
    print(f"{j} - {dict[j]}",end=" ")
    n += 1
    if n % 5 == 0:
        print()

