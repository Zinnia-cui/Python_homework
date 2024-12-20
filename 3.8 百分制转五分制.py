s=eval(input())
if s < 0.0 or s > 100.0:
    print("Not valid")
elif s >= 90.0:
    print("A")
elif s >= 80.0:
    print("B")
elif s >= 70.0:
    print("C")
elif s >= 60.0:
    print("D")
else:
    print("E")


