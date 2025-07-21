import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    data = {'Name':['Amit','Sagar','Pooja'],
            'Math':[85,90,78],
            'Science':[92,88,80],
            'English':[75,85,82]
            }
    
    df = pd.DataFrame(data)

    data2 = {'Name':['Amit','Sagar','Pooja'],
            'Math':[np.nan,76,88],
            'Science':[91,np.nan,85]
            }
    
    df2 = pd.DataFrame(data2)

    df2[['Math','Science']]=df2[['Math','Science']].fillna(df2[['Math','Science']].mean())
    print(df)

   
if __name__=="__main__":
    main()

