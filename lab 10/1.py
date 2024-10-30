import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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

# distribution of continous features
continous_features = df.select_dtypes(include=[np.number]).columns.tolist()

num_features = len(continous_features)
row = (num_features // 3) + (num_features % 3 > 0)

plt.figure(figsize=(15,10))
for i, column in enumerate(continous_features[:9]):
    plt.subplot(3,3, i+1)
    sb.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")

plt.tight_layout() 
plt.show()





