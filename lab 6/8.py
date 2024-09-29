import pandas as pd

f1 = r'Pandas\\lab 6\\orders.csv'
f2 = r'Pandas\\lab 6\\products.csv'

orders = pd.read_csv(f1)
products = pd.read_csv(f2)

# b
print("The first 5 rows of Orders are: ")
print( orders.head(5))
print("\nThe last 10 rows of Orders are: ")
print(orders.tail(10))

print("\nThe first 5 rows of Products are: " )
print(products.head(5))
print("\nTHe last 10 rows of Products are: ")
print(products.tail(10))

# c
orders['Revenue'] = orders['Quantity'] * products['Price']

total_revenue = orders['Revenue'].sum()
print("The total revenue is: ")
print(total_revenue)

# d 
products['sortedProducts'] = products.sort_values(by)



