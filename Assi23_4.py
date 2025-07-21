import pandas as pd

def main():
    data = {'Name':['Amit','Sagar','Pooja'],
            'Math':[85,90,78],
            'Science':[92,88,80],
            'English':[75,85,82]
            }
    
    df = pd.DataFrame(data)
    
    print("The student who scored more than 85 is :")

    Name_of_student = df[df['Science']>85]
    print(Name_of_student)
    
if __name__=="__main__":
    main()