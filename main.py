import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')

df['User_Score'] = pd.to_numeric(df['User_Score'], errors='coerce')

df_clean = df.dropna(subset=['Global_Sales', 'Critic_Score', 'User_Score']).copy()

corr_matrix = df_clean[['Global_Sales', 'Critic_Score', 'User_Score']].corr(method='pearson')
print("--- Matriks Korelasi ---")
print(corr_matrix)

X = df_clean[['Critic_Score', 'User_Score']]
X = sm.add_constant(X)
Y = df_clean['Global_Sales']

model = sm.OLS(Y, X).fit()

print("\n--- Ringkasan Model Regresi ---")
print(model.summary())

plt.figure(figsize=(10, 6))
sns.regplot(x='Critic_Score', y='Global_Sales', data=df_clean, 
            scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
plt.title('Gambar 2. Scatter Plot dan Garis Regresi Critic Score terhadap Global Sales')
plt.xlabel('Critic Score (X1)')
plt.ylabel('Global Sales (Y)')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='Blues', fmt='.3f')
plt.title('Gambar 3. Heatmap Korelasi Variabel')
plt.show()