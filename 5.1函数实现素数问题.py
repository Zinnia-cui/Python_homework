def isPrime(number): # 判断一个数是否为素数
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def printPrimeNumbers(num1, num2, numbersOfLine): # 打印num1到num2之间的所有素数，每行输出numbersOfLine个
    count = 0
    for i in range(num1, num2 + 1):
        if isPrime(i):
            print(f"{i:6d}", end="")  # 用f-string格式化输出，确保占6列
            count += 1
            if count % numbersOfLine == 0:  # 每输出numberOfLine个素数换行
                print()
    if count % numbersOfLine != 0:  # 如果最后一行不满numberOfLine个素数，换行
        print()

def main():
    num1=int(input())
    num2=int(input())
    numOfLine=int(input())
    printPrimeNumbers(num1,num2,numOfLine)
main() # 调用main函数

