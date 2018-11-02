#-*-coding:utf-8-*-

import pandas as pd

df1 = pd.read_csv('pcauto_sales.csv')
df2 = pd.read_csv('pcauto_sales_add.csv')

#new_csv = pd.merge(df1,df2,how='left',left_on='car_type',right_on='autohome_series')
new_csv = pd.concat([df1,df2],axis=1,join='inner')
new_csv.to_csv('pcauto_sales_new.csv',index=False)
