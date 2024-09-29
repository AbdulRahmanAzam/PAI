import pandas as pd

data = {
    'Movie': ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'],
    'Runtime': [120, 150, 90, 110, 130]  
}


df = pd.DataFrame(data)

sorted_data = df.sort_values(by='Runtime', ascending=False)

print(sorted_data)
