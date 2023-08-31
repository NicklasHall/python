import os   

os.system('cls')


x=input("skriv")

for i in range(10):
    print(x)


y=1 
 
while True:
    print(y)
    if y == 10: 
        break
    y += 1 


y2=1
x2=int(input("vilket tal vill du ha"))
while True:
    print(x2)
    y2 +=1 
    if y2 == x2:
        break


for table in range(1, 13):  #tolv tabeller
    print(f"TABELL {table}")
    for y in range(1, 11):  #tio tal i varje
        print(f"{table} * {y} = {str(table * y)}")

        
    