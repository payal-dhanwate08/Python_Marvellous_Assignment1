import pandas as pd 
from sklearn.model_selection import train_test_split

def main():
    data={'Age':[22,25,47,52,46,56],'purchased':[0,1,1,0,1,0]}
    
    df = pd.DataFrame(data)
    x=df[['Age']]
    y=df[['purchased']]
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.5,random_state=42)
    print("x_train",x_train)
    print("x_test",x_test)
    print("y_train",y_train)
    print("y_test",y_test)

if __name__=="__main__":
    main()