f = open("Lab 2/text.txt", "r")

read = f.read()

char = len(read)

words = read.split()
word_count = len(words)

print(f"The characters are = {char}\n and the words are {word_count}")