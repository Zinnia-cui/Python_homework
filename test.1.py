students=[]

with open ('data.txt','r',encoding='utf-8') as df:
      next(df)
      for line in df:
            data = line.strip().split(',')
            name = data[2]
            score=list(map(int,data[4:]))
            if any(score<60 for score in scores):
                  students.append(name)

for name in students:
      print(name)


