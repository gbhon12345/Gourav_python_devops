print("Hello Gourav")

env = input("Enter the env where do you want to run your code: ")

print(" We are running this code in ",env,"environment")

if env == 'prod':
    print (" Don't Deploy on Friday and weekend")
elif env == 'stg':
    print("Take Back up and Test well if fails resotre the backup make sure its should be in zero downtime")
else:
    print("Its Safe to deploy on today..!")

a = int(input("Enter your 1st number:"))
          
b = int(input("Emter your 2nd number: "))

print(" Addition of a and b:", a + b)
print(" Substration of a and b:", a - b)
print(" Multiplication of a and b:", a * b)
print(" a divided by b is:", a / b)
