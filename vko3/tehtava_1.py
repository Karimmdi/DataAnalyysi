import pandas as pd
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt

# Lue tiedostot
df_emp = pd.read_csv('employees.csv', header=0, sep=',', dtype={'phone1': str, 'phone2': str})
df_dep = pd.read_csv('departments.csv', header=0, sep=',')

# Yhteenveto numeerisista tiedoista
emp_desc = df_emp.describe()

# Laske puuttuvat arvot
emp_nans = df_emp.isna().sum()

# Suurimmat palkat
emp_suur_palkpalk = df_emp.nlargest(5, 'salary')

# Printataan tulokset
print(df_emp['fname'].info())  # Tämä tulostaa sarakkeen tietotyypit, mutta ei arvoja

print(emp_desc)  # Yhteenveto numeerisista arvoista

print(emp_suur_palkpalk)  # 5 suurinta palkkaa

print(df_emp['salary'].nsmallest(5))  # 5 pienintä palkkaa

# Yhdistetään employee ja department dataframe
df = pd.merge(df_emp, df_dep, how='inner', on='dep')

# Poistetaan sarake 'image'
df.drop(columns=['image'], inplace=True)

# Tehtävä 2:
# Lasketaan työntekijöiden määrä
n_emp = df['id'].count()

# Miesten määrä ja prosentti
male = df[(df['gender'] == 0) & (df['dname'] == 'Tuotanto')].shape[0]
male_pro = (male / n_emp) * 100

# Naisten määrä ja prosentti
female = (df['gender'] == 1).sum()
female_pro = (female / n_emp) * 100

print(f"Työntekijöiden määrä: {n_emp}")
print(f"Miehiä: {male} ({male_pro:.1f}%)")
print(f"Naisten määrä: {female} ({female_pro:.1f}%)")

min_palkka = df['salary'].min()
max_palkka = df['salary'].max()
avg_palkka = df['salary'].mean()

print(f"minimi palkka: {min_palkka}€")
print(f"maksimi palkka: {max_palkka}€")
print(f"Keskipalkka: {avg_palkka:.2f}€")

tuotekehitys = df[df['dname'] == 'Tuotekehitys']
avg_palk_tuotekehitys = tuotekehitys['salary']. mean()

print(f"Tuotekehityksen osaston keskipalkka: {avg_palk_tuotekehitys:.2f}€")

no_phone2 = df['phone2'].isna().sum()
print(f"Työntekijöitä, joilla ei ole kakkospuhelinta: {no_phone2}")

df['age'] = (datetime.now() - pd.to_datetime(df['bdate'])) // timedelta(days=365.2425)
print(df[['fname', 'bdate', 'age']].head())

df['age_group'] = (df['age'] // 5 + 1) * 5
df['age_group'] = df['age_group'].where(df['age_group'] < 70, 70)
print(df[['fname', 'age', 'age_group']].head())

df_corr = df[['salary', 'age', 'gender']]

corr_matriisi = df_corr.corr()

plt.figure(figsize=(6, 4))

sns.heatmap(corr_matriisi, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1,vmax=1 )
plt.title('Korrelaatiomatriisi (salary, age, gender)')
plt.show()











