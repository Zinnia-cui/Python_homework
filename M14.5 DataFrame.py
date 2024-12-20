import pandas as pd
import numpy as np
def main():
    df = pd.DataFrame({
        'A': [1.0, 2.0, 3.0, 4.0]
        ,
        'B': ['2013-01-02', '2013-01-02', '2013-01-02', '2013-01-02']
        ,
        'C': [1.0, 1.0, 1.0, 1.0]
        ,
        'D': [3, 3, 3, 3]
        ,
        'E': ['test', 'train', 'test', 'test']
        ,
        'F': ['foo', 'foo', 'foo', 'foo']
    })
    print(df)


if __name__ == '__main__':
    main()