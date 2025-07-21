import pandas as pd 
import numpy as np

def main():
    data = {'Name':['Amit','Sagar','Pooja'],
            'Math':[85,90,78],
            'Science':[92,88,80],
            'English':[75,85,82]
            }
    
    df = pd.DataFrame(data)
    df['Gender']=['male','male','female']
    print(df)

    Marks = ['Math','Science','English']
    Average_Marks_by_Student = df.groupby('Gender')[Marks].mean()
    print("Calculating Average Marks:")
    print(Average_Marks_by_Student)


if __name__=="__main__":
    main()