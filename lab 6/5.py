import pandas as pd

# Correct the file path
with open(r"Pandas\\lab 6\\world_alcohol_consumption.csv") as f:
    
    df = pd.read_csv(f)

    
    print("The dataFrame is:")
    print(df)

    print("\nShape of the dataset is:")
    print(df.shape)

    column_names = df.columns.tolist()

    print("\n\nThe names of the columns are: ")
    print(column_names)
