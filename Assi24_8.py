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
 
    plt.hist(df['Math'],bins=5,color='blue',edgecolor='black')
    plt.title('histogram for student marks')
    plt.xlabel('Math marks')
    plt.ylabel('All student')
    plt.show()

if __name__=="__main__":
    main()