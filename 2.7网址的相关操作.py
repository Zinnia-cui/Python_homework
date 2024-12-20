s=input()
print(s.upper())
print(s.endswith('org'))
print(s.startswith('www'))
a=s.count('.')
if a>0:
    print('True',a)
else:
    print('False',a)
print(s.isdigit())

a=input()
b=a.upper()
print(b)
print(a.endswith('org'))
print(a.startswith('www'))
c=a.count('.')
d="."in a
print(d,c)
e=a.isnumeric()
print(e)