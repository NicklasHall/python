try:
    with open("test.txt") as my_file:
        content=my_file.read() 

    print(content)
except:
    print("filen finns inte")


    