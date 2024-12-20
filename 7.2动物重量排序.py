'''def weightUnit(weight):
    if weight[-1] == 't':
        return float(weight[:-1]) * 1000
    else:
        return float(weight[:-2])

def main():
    animals = []
    while True:
        user_input = input()
        if user_input == "-1":
            break
        else:
            name, weight = user_input.split()
            animals.append([name, weight])
    animals.sort(key=lambda x: weightUnit(x[1]))
    result = [[name, w] for name, w in animals]
    print(result)

if __name__ == "__main__":
    main()'''
'''
海豚 228kg
北极熊 0.75t
企鹅 35kg
海豹 0.35t
白鲸 1.35t
-1
'''
res=[]
while True:
    t=input()
    if t=='-1':
        break
    res.append(t.split())
res=sorted(res,key=lambda x : float(x[1][0:-1])*1000 if x[1][-1]=='t' else float(x[1][0:-2]))
print(res)

