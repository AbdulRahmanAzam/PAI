import pandas as pd

data = {
    'Movie': ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'],
    'Revenue': [3000000, 500000, 2500000, 4000000, 700000],
    'Budget': [800000, 1200000, 700000, 900000, 1500000]
}

df = pd.DataFrame(data)

rev = df[(df['Revenue'] > 2000000) & (df['Budget'] < 1000000)]

print(rev)