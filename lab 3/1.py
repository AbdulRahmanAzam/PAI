try:

    with open(r"c:\\Users\\k230061\Desktop\\1.py\\1.txt") as f:
        text = f.read()

        # method 1
        cnt = 0
        for i in text:
            cnt+=1

        # method 2
        cnt = len(text)

        print(f"the number of characters are {cnt}")

        # method 1
        cnt = 0
        for i in text.split():
            cnt+=1

        # method 2
        cnt = len(text.split())

        print(f"The number of word count are {cnt}")

        print(text)

except Exception as e:
    print("Error : " + str(e))