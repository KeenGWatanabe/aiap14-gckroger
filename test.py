import pandas as pd
import numpy as np
dates = pd.date_range('1/1/2000', periods=8)

df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

print(df)
a = df['A']
print(a[dates[5]])
b = df['A']
print(b[dates[6]])
c = df['B']
print(c[dates[5]])
d = df['B']
print(d[dates[5]])


