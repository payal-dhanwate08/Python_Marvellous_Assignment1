import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score


def Diabetes(Datapath):
    df = pd.read_csv(Datapath)
    print(df.head())
    print("column info")
    print(df.info())
    print("check the null value in the dataset")
    print(df.isnull().sum)
    print("Basic statistics")
    print(df.describe())

    plt.figure(figsize=(6,4))
    sns.countplot(data=df,x='Outcome')
    plt.xlabel("target variable category")
    plt.ylabel("count")
    plt.title("Dostribution of the target variable")
    plt.show()

    plt.figure(figsize=(12,10))
    plt.hist(df,bins=30,edgecolor='black')
    plt.title("Histogram")
    plt.show()

    plt.figure(figsize=(15,10))
    sns.pairplot(df,hue="Outcome")
    plt.show()

    columns = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction']
    print("zero value",columns==0)
    df[columns]=df[columns].replace(0,np.nan)
    print(df.head())
    df[columns]=df[columns].fillna(df[columns].median())

    scaler = StandardScaler()
    x = df.drop(columns = ['Outcome'])
    y = df['Outcome']
    scaler_data = scaler.fit_transform(x)
    print("After applying feature scaling")
    print(scaler_data)

    x_train, x_test, y_train, y_test = train_test_split(scaler_data,y,test_size=0.2,random_state=42)

    model = LogisticRegression()
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    Accuracy = accuracy_score(y_test,y_pred)
    print("LogisticRegression")
    print("Accuracy is:",Accuracy)
    precision = precision_score(y_test,y_pred)
    print("Precision score is :",precision)
    Recall = recall_score(y_test,y_pred)
    print("Recall score is :",Recall)
    F1 = f1_score(y_test,y_pred)
    print("f1 score is :",F1)
    Confusion_matrix = confusion_matrix(y_test,y_pred)
    print("confusion matrix is :")
    print(Confusion_matrix)

    plt.figure(figsize=(6,5))
    sns.heatmap(Confusion_matrix,annot=True,fmt='d',cmap='Blues',cbar=True)
    plt.xlabel("predicted")
    plt.ylabel("Actual")
    plt.title("confusion matrix of LogisticRegression")
    plt.show()

    model_2 = KNeighborsClassifier()
    model_2.fit(x_train,y_train)
    y_pred = model_2.predict(x_test)
    print("KNN classifier")
    print("Accuracy is :",Accuracy)
    precision = precision_score(y_test,y_pred)
    print("Precision score is :",precision)
    Recall = recall_score(y_test,y_pred)
    print("Recall score is :",Recall)
    F1 = f1_score(y_test,y_pred)
    print("f1 score is :",F1)
    Confusion_matrix = confusion_matrix(y_test,y_pred)
    print("confusion matrix is")
    print(Confusion_matrix)

    plt.figure(figsize=(6,5))
    sns.heatmap(Confusion_matrix,annot=True,fmt='d',cmap='Blues',cbar=True)
    plt.xlabel("predicted")
    plt.ylabel("Actual")
    plt.title("confusion matrix of LogisticRegression")
    plt.show()

    print("Result is :",model.predict([[3,126,88,41,235,39.3,0.704,27],[7,147,76,0,0,39.4,0.257,43]]))
    df.to_csv("Diabetiesdetails.csv",index=False)


def main():
    Diabetes("diabetes.csv")
    
if __name__=="__main__":
    main()