try:

    with open(r"c:\\Users\\k230061\Desktop\\1.py\\2.txt") as f:
        text = f.read()

        newcontent = text.replace("wow", "wow kia kehne hen sir jee")

        print(newcontent)

    with open(r"c:\\Users\\k230061\Desktop\\1.py\\2.txt", "w") as f:
        f.write(newcontent)

except Exception as e:
    print("Error : " + str(e))