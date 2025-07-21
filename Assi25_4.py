import pandas as pd

def main():
    data = {'Department':['HR','IT','Finance','HR','IT']}
    df = pd.DataFrame(data)

    encoded = pd.get_dummies(df['Department'])
    print(encoded)

if __name__=="__main__":
    main()