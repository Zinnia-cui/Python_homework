def whileGCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def forGCD(a,b):
    if a < b:
        a, b = b, a
    for i in range(b,0,-1):
        if a%i == 0 and b%i == 0:
            return i