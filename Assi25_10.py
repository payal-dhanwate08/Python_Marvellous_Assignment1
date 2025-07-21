import pandas as pd 
from sklearn.model_selection import train_test_split

def main():
    data={'Age':[25,30,45,35,22],'salary':[50000,60000,80000,650000,450000],'purchased':[1,0,1,0,1]}
    
    df = pd.DataFrame(data)

    x=df[['Age','salary']]
    y=df[['purchased']]
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
    print("x_train data",x_train)
    print("x_test data",x_test)
    print("y_train data",y_train)
    print("y_test data",y_test)

if __name__=="__main__":
    main()