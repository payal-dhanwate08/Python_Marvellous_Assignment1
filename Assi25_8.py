import numpy as np 
import pandas as pd

def main():
    data = {'Marks':[85,np.nan,90,np.nan,95]}
    df=pd.DataFrame(data)
    null_value=df['Marks'].interpolate()
    print(null_value)
  

if __name__=="__main__":
    main()