import pandas as pd

with open(r'Pandas\\lab 6\\world_alcohol_consumption.csv') as f:
    df = pd.read_csv(f)

    alc = df[(df['Year'] == 1985) | (df['Year'] ==  1986)]

    print(alc)

