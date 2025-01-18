import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('diabetes.csv')

print("Lukumäärä (count):\n", df.count())
print("Keskiarvo (mean):\n", df.mean())

desc = df.describe()
corr = df.corr()

df.hist(bins=20, figsize=(12, 10), color='skyblue', edgecolor='black')
plt.suptitle('Histogrammi datasta', fontsize=16)
plt.tight_layout()
plt.show()

sns.heatmap(corr, annot=True, cbar=False)
plt.show()

#Tehtävä 9
age_counts = df['Age'].value_counts().sort_values(ascending=False)
print("Potilaiden lukumäärä iän mukaan (laskeva järjestys):")
print(age_counts)


diabetes_tapaukset = df['Outcome'].value_counts()
print("\nDiabetestapaukset ja ei-diabetestapaukset:")
print(f"Ei-diabetesta (0): {diabetes_tapaukset[0]}")
print(f"Diabetesta (1): {diabetes_tapaukset[1]}")

#Tehtävä 10
nan_counts = df.isna().sum()
print("\nNaN-arvot sarakkeessa")
print(nan_counts[nan_counts > 0])



