import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def main():
    data = {'Name':['Amit','Sagar','Pooja'],
            'Math':[85,90,78],
            'Science':[92,88,80],
            'English':[75,85,82]
            }
    
    df = pd.DataFrame(data)

    df['Total'] = df[['Math','Science','English']].sum(axis='columns')
    print("Total marks")
    print(df)

    df['Status']=df['Total'].apply(lambda x:'pass'if x>250 else 'fail')
    print("Display the pass or fail status")
    print(df)
 

    count = (df['Status'].value_counts()['pass'])
    print("The number of student who pass :",count)

if __name__=="__main__":
    main()