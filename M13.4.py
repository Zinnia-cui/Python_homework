# 定义一个程序，读取文本文件中的唯一单词，去除非字母字符，将结果输出到另一个文件
words = set()  # 使用集合来存储唯一单词
with open('in.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # 处理每一行，去除非字母字符并转为小写
        word = []
        for char in line:
            if char.isalpha():
                word.append(char.lower())
            elif char.isspace():
                word.append(' ')
            else:  # 对于其他字符
                word.append(' ')
        clean_line = ''.join(word)
        clean_line = clean_line.strip()
        words.update(clean_line.split())  # 直接更新集合，无需额外变量
# 将词汇表按字典顺序排序
sorted_words = sorted(words)

# 输出到新文件
with open('words.txt', 'w', encoding='utf-8') as of:
    for w in sorted_words:
        of.write(f"{w}\n")