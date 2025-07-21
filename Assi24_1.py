import pandas as pd 
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def main():
    data = {'Name':['Amit','Sagar','Pooja'],
            'Math':[85,90,78],
            'Science':[92,88,80],
            'English':[75,85,82]
            }
    
    df = pd.DataFrame(data)
    scalar = MinMaxScaler()
    print("Dataframe befor normalization ")
    print(df)

    df['Math']=scalar.fit_transform(df[['Math']])
    print("Dataframe after normlization")
    print(df)
   

if __name__=="__main__":
    main()