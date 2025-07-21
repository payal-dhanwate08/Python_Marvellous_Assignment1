import numpy as np 
import pandas as pd

def main():
    data = {'Age':[18,22,25,30,35]}
    df = pd.DataFrame(data)
    orignal_value=df['Age']
    min_value=df['Age'].min()
    min_value=df['Age'].max()

    normalized = (orignal_value-min_value)/(min_value-min_value)
    print(normalized)

if __name__=="__main__":
    main()