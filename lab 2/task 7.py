temperatures = [28,34,45,23,29,28,34,45,23,29,28,34,45,23,29,28,34,45,23,29,28,34,45,23,29,28,34,45,23,29]

def avg(temp):
    sum = 0
    
    for i in temp:
        sum += i
    
    return sum / 30

print("The average of temperatures for the month is = ", avg(temperatures))

print(f"The highest temperature is = {max(temperatures)} and the lowest temperature is = {min(temperatures)}")

print(f"The sorted temperatures are = {temperatures}")

del temperatures[5]
print(f"After deleting the 6th element, the list is = {temperatures}")
