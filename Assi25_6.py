import pandas as pd 
def main():
    data={'Grade':['A+','B','A','C','B+']}
    df = pd.DataFrame(data)

    mapping_data = {'A+':'Excellent',
                    'A':'very Good',
                    'B+':'Good',
                    'B':'Average',
                    'C':'poor'
                    }
    
    df['Grade']=df['Grade'].replace(mapping_data)
    print(df)

if __name__=="__main__":
    main()