import numpy as np
import pandas as pd

def main():
    data = {'salary':[25000,27000,29000,31000,50000,100000]}
    df = pd.DataFrame(data)
    sort_data = np.sort(df)
    print(sort_data)
    Q1 = df['salary'].quantile(0.25)
    Q3 = df['salary'].quantile(0.75)

    IQR = Q3-Q1
    low =Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    outlier = df[(df['salary']<low)|(df['salary']>upper)]
    print("outlier in the dataframe is:")
    print(outlier)

if __name__=="__main__":
    main()