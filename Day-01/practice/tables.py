#num= int(input("Enter number: "))
n=0
while(n<5):
    num= int(input("Enter number: "))
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
    n=(n+1)   
