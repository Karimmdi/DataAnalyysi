import pandas as pd
from datetime import datetime, timedelta
df_emp = pd.read_csv('employees.csv', dtype={'phone1':str, 'phone2':str})
emp_desc = df_emp.describe()
emp_nans = df_emp.isna().sum()

df_dep = pd.read_csv('departments.csv')

print(df_emp['lname'].unique())
print(df_emp['fname'].isnull())
print(df_emp['fname'].info())
print(df_emp['fname'].describe())
print(df_emp['salary'].nlargest(5))
print(df_emp['salary'].nsmallest(5))


df = pd.merge(df_emp, df_dep, how='inner', on='dep')

df.drop(columns=['image'], inplace=True)  #poistaa haluttu sarakke

n_emp= df['id'].count()
n_emp = df.id.count()
male = df[(df['gender'] == 0) & (df['dname'] == 'Tuotanto')].shape[0]

female = (df['gender'] == 1).sum()

df['age'] = (datetime.now() - pd.to_datetime(df['bdate'])) // timedelta(days=365.2425)











