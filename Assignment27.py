import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def Advertisment(Datapath):
    df = pd.read_csv(Datapath)
    print(df.head())

    df.drop(columns=["Unnamed: 0"],inplace=True)
    print(df.head())

    x = df[['TV','radio','newspaper']]
    y = df['sales']

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42) 
    model = LinearRegression()
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    print("Expected value is",y_test)
    print("Predicted value is",y_pred)
    
  
def main():
    Advertisment("Advertising.csv")

if __name__=="__main__":
    main()
