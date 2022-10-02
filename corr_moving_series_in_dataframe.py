    
#################################################
import pandas as pd 
import numpy as np
import scipy as sp 
import time ,os 
import matplotlib.pyplot as plt

store_corr=[] #empty list to store the rolling correlation of each pairs
names=[] #empty list to store the column name
df=df.pct_change(periods=1).dropna(axis=0) #Prepate dataframe of time series

for i in range(0,len(df.columns)):

    for j in range(i,len(df.columns)):
        corr = df[df.columns[i]].rolling(20).corr(df[df.columns[j]]) # here we use what ever integer-based period we want and rolling method
        #    OR     corr = df[df.columns[i]].rolling(20).corr(df[df.columns[j]])
        names.append('col '+str(i)+' -col '+str(j))
        store_corr.append(corr)
        df_corr=pd.DataFrame(np.transpose(np.array(store_corr)),columns=names)
        
        
        #############################################################end here 
        
        

    
   