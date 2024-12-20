import pandas as pd
import numpy as np

def main():
    np.random.seed(0)
    dates = pd.date_range('20200101', periods=10)
    df = pd.DataFrame(np.random.randn(10, 4), index=dates, columns=list('ABCD'))
    print(df.index)



if __name__ == '__main__':
    main()