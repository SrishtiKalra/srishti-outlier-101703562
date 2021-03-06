import pandas as pd

def row_removal(dataset,newdataset):
    import numpy as np
    import math as m
    dataset=pd.DataFrame(dataset)
    
    no_row=dataset.shape[0]  #calculating the number of rows
    no_col=dataset.shape[1]  #calculating the number of columns    

    for i in range(0,no_col):
        x=list(dataset.columns)
        j=dataset.sort_values(by=x[i])
        y=j.iloc[:,i].values
        
        no_row=dataset.shape[0]
        no_col=dataset.shape[1]
        
        s=m.floor((no_row+1)/4)
        t=m.ceil((no_col+1)/4)
        Q1=(y[s-1]+y[t-1])/2  #finding Quartile Q1
        

        q=m.floor(3*(no_row+1)/4)  
        w=m.ceil(3*(no_row+1)/4)
        Q3=(y[q-1]+y[w-1])/2  #finding Quartile Q3
        

        IQR=Q3-Q1  #finding Inter Quartile Range
        
        Min=Q1-1.5*IQR  #finding Max
        Max=Q3+1.5*IQR  #finding Min
    

        for k in range(0,no_row):   
            if y[k]<Min:
                dataset = dataset.drop([k])  #removing Outliers less than Min
            if y[k]>Max:
                dataset = dataset.drop([k])
        dataset.index = np.arange(0,len(dataset))  #removing Outliers greater than Max 
                

    dataset.to_csv(newdataset)

import sys 

def main():
    dataset=pd.read_csv(sys.argv[1]).values
    newdataset=sys.argv[2]
    row_removal(dataset,newdataset)
    

if __name__=="__main__":
     main()