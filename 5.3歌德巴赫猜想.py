def isPrime(i):   #判断一个数字是否是素数
    if i < 2:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

def main():
    n = int(input( ))
    for even in range(4, n+1, 2): #遍历从4开始的偶数
        for i in range(2, even):
            if isPrime(i) and isPrime(even-i) and i<= even-i: #判断两个素数是否满足歌德巴赫猜想
                print(f"{even}={i}+{even-i}")
                break  # 找到一个素数对后跳出循环

main()



