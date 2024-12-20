s=input()
lower_count = 0
upper_count = 0
digit_count = 0
space_count = 0
other_count = 0
for i in s:
    if i.islower():
        lower_count +=1
    elif i.isupper():
        upper_count +=1
    elif i.isdigit():
        digit_count +=1
    elif i.isspace():
        space_count +=1
    else:
        other_count +=1
print(lower_count,upper_count,digit_count,space_count,other_count)

