tocurrency = input("Which of the following currency you want to convert?\nEuro\nDollar\nPKR\nINR\nYen\n: ")

amount = int(input("Enter the amount you want to convert: "))

fromcurrency = input("In which currency you want to convert?: ")

print(f"Converting {amount} from {fromcurrency} to {tocurrency}")
