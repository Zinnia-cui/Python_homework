with open('air_passengers.csv', 'w') as f:
    f.write('q')
import pandas as pd
def main():
    file_name = 'air_passengers.csv'
    df = pd.read_csv(file_name)
    pd1 = df.head(5)
    pd1.to_csv('result.csv', index=False)
    # print(pd.read_csv('macrodata.csv').head())

if __name__ == '__main__':
    main()

