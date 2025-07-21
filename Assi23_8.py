import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {'Name':['Amit','Sagar','Pooja'],
            'Math':[85,90,78],
            'Science':[92,88,80],
            'English':[75,85,82]
            }
    
    df = pd.DataFrame(data)

    marks = df[df['Name']=='Amit'][['Math','Science','English']].values.flatten()
    subjects = ['Math','Science','English']

    plt.plot(subjects,marks,marker ='o')
    plt.xlabel("Subject")
    plt.ylabel("mark")
    plt.title("Amit report")
    plt.grid(True)
    plt.show()

if __name__=="__main__":
    main()

   