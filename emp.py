import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-12/Downloads/Department_Dataset.csv")
print(data)

#print male employee working in cs baranch
info=data[data['gender']=='male']
print(info[info['Dept']=='CS'])

#print female employee working in ee branch
info=data[data['gender']=='female']
print(info[info['Dept']=='EE'])

#print the sum of salary of employee in each  departmemt
print(data.groupby('Dept')['salary']. sum())

