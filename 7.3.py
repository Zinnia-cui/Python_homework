mtx = [
   [1,  1,  1,  1],
   [2,  2,  2,  2],
   [3,  3,  3,  3],
   [4,  4,  4,  4]
]
sum = 0
for i in range(4):
    sum += mtx[i][i] #主对角线
for i in range(4):
    sum += mtx[i][3-i] #副对角线
print(sum)

