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
  
    all_subject =['Math','Science','English']
    all_marks = [90,88,85]
    plt.figure(figsize=(8,5))
    plt.pie(all_marks,labels=all_subject)
    plt.title("Pie chart of subject marks")
    plt.show()
    
if __name__=="__main__":
    main()