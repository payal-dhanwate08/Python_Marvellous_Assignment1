import pandas as pd

def main():
    data = {'Name':['A','B','c'],'Age':[21.0,22.0,23.0]}
    df = pd.DataFrame(data)

    print("Befor coversion of data type")
    print(df.dtypes)

    df['Age']=df['Age'].astype(int)
    print("After conversion of data type")
    print(df.dtypes)

if __name__=="__main__":
    main()