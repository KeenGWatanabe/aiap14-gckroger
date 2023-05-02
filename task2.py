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

#create boolean column for 60% humidity
df['60humid'] = np.where(df['Humidity9am'] >= 60, 1,0)

#create boolean column for Cloud count above 6
df['highcloud'] = np.where(df['Cloud9am'] >= 7, 1,0)

#index column
df['count'] = 1

#create probability dataframe from above
df = df[['60humid', 'highcloud','count']]
df.head()

#create a pivot table from above
dfl = pd.pivot_table(df, values='count', index=['60humid'], columns=['highcloud'], aggfunc=np.size,fill_value=0)

#print pivot table
print(dfl)

#assigning pivot table values for probability calculation
A1 = dfl.loc[[0],[0]]
dtype: A1
#B1 = dfl.loc[[0],[1]]

#C1 = dfl.loc[[1],[0]]

#D1 = dfl.loc[[1],[1]]

#defining PA, PB, PandB
#PA = (B1+D1)/(A1+B1+C1+D1)
#print(PA)
#PB = (C1+B1)/(A1+B1+C1+D1)
#PandB = D1/(A1+B1+C1+D1)
#result = PandB/PB
#print(result)


