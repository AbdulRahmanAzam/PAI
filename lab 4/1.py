a = ["He", "th", "i", "sal"]
b = ["llo","is","s","man"]

# one line method
c = [a + b for a,b in zip(a, b)]

# lengthy method
d = []
for i in range(len(a)):
    d.append(a[i] + b[i])

print(c)
print(d)
