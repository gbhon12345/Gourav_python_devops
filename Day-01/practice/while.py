
choice=input("Enter your choice(q for quite): ")


while(choice != "q"):
    num= int(input("Enter number: "))
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
    choice=input("Enter your choice(q for quite): ")   
