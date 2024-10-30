import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv('heart.csv')

# loading dataset
print(df.head())
print(df.info())
print(df.describe())

# visualizing target variable
plt.figure(figsize=(8,6))
sb.countplot(x='target', data=df)
plt.title("Distributoin of Heart Disease")
plt.xlabel('Heart Disease ')
plt.ylabel('Count')
plt.show()





