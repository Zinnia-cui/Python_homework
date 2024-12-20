import pandas as pd
import numpy as np


def main():
    arr1, arr2, arr3, arr4 = input().split()
    arr1 = int(arr1)
    arr2 = int(arr2)
    arr3 = int(arr3)
    arr4 = int(arr4)
    np.random.seed(0)
    dates = pd.date_range('20200101', periods=366)
    df = pd.DataFrame(np.random.randn(366, 4), index=dates, columns=list('ABCD'))
    print(df.iloc[[arr1-1,arr2-1], [arr3-1,arr4-1]])

if __name__ == '__main__':
    main()