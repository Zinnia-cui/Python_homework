n=int(input())
d = {}
for i in range(n):
    word, trans = input().split()
    d[word] = trans
    # word是键key，trans是值value
word = input()
if word in d:
    print(d[word])
else:
    print("not found")

