import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def MarvellousPlayPredictor(Datapath):
    df = pd.read_csv(Datapath)

    label_encoder = LabelEncoder()
    df["Whether"] = label_encoder.fit_transform(df["Whether"])
    df["Temperature"] = label_encoder.fit_transform(df["Temperature"])
    print("After manipulating data",df)

    x = df[['Whether','Temperature']]
    y = df['Play']

    print("Clean the Dataset")
    df.drop(columns = ["Unnamed: 0"],inplace=True)
    print(df)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x,y) #train data
    print("Result is",model.predict([[2,1],[2,1]])) 

def CheckAccuracy(value):
   
    df = pd.read_csv("PlayPredictor.csv")
    label_encoder = LabelEncoder()

    df["Whether"] = label_encoder.fit_transform(df["Whether"])
    df["Temperature"] = label_encoder.fit_transform(df["Temperature"])

    x = df[['Whether','Temperature']]
    y = df['Play']

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42) 
    model = KNeighborsClassifier(n_neighbors=value)

    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    
    Accuracy = accuracy_score(y_test,y_pred)
    print("Accuracy score is ",Accuracy*100)

def main():
    MarvellousPlayPredictor("PlayPredictor.csv")
    CheckAccuracy(15)

if __name__=="__main__":
    main()