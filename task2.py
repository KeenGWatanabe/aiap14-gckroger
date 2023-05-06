# -*- coding: utf-8 -*-
"""
@author: rgerweb
"""
import pandas as pd
import numpy as np

#testing data read with csv
df = pd.read_csv('data/fishing.csv', index_col = 0)
#check data type of table
df.dtypes
df.query('Rainfall >= 10')
#print(df)
#create boolean column for 60% humidity
df['60humid'] = np.where(df['Humidity9am'] >= 60, 1,0)

#create boolean column for Cloud count above 6
df['highcloud'] = np.where(df['Cloud9am'] >= 7, 1,0)

#index column
df['count'] = 1

#assigning pivot table values for probability calculation

#create probability dataframe from above
df = df[['60humid', 'highcloud','count']]
df.head()

#create a pivot table from above
dfl = pd.pivot_table(df, values='count', index=['60humid'], columns=['highcloud'], aggfunc=np.size,fill_value=0)

#print pivot table
print(dfl)


A = dfl.values[0,0]
B = dfl.values[0,1]
C = dfl.values[1,0]
D = dfl.values[1,1]
print("A=",A,"B=",B,"C=",C,"D=",D)
#defining PA, PB, PandB
PA = (C+D)/(A+B+C+D)
#print(PA)
PB = (B+D)/(A+B+C+D)
PAB = D/(A+B+C+D)
result = PAB/PB
print(round(result*100,2), "percent probability")


