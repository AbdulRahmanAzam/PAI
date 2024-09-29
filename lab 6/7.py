import pandas as pd

f = r"Pandas\\lab 6\\employee_data.xlsx"

df = pd.read_excel(f)

print("The data of All employees are: ")
print(df)

print("The data of the Employee of year 2019")

# ensuring that startDate is in string, then only we can find the last 2 digits of full date
df['StartDate'] = df['StartDate'].astype(str)

# getting the year by -2: and check for the year 2019
year = df[(df['StartDate'].str[-2:]) == '19']

print(year)



