import numpy as np
def main():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    n = int(input())
    a_array = np.array(a)
    b_array = np.array(b)
    r1 = a_array + n
    r2 = a_array + b_array
    r3 = a_array * b_array
    r4 = a_array ** b_array
    print(r1)
    print(r2)
    print(r3)
    print(r4)
if __name__ == '__main__':
    main()


    