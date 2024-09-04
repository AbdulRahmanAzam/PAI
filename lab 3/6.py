try:
    text = input("Enter sentence")

    if(text.find("?")):
        with open(r"c:\\Users\\k230061\Desktop\\1.py\\6questionquestions.txt", "w") as f:
            f.write(text)
            
except Exception as e:
    print("Error : " + str(e))