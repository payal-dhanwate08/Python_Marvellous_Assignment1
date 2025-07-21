import pandas as pd

def main():
    data = {'City':['Pune','Mumbai','Delhi','Pune','Delhi']}

    df = pd.DataFrame(data)
    City = ['Pune','Mumbai','Delhi','Pune','Delhi']
    df['City']=City
    df['City']=df['City'].map({'Pune':0,'Mumbai':1,'Delhi':2})
    print("After encoding")
    print(df)

if __name__=="__main__":
    main()