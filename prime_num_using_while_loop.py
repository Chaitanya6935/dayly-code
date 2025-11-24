x = int(input("Enter any number : "))

y = 2
while x!=y:
    if x%y==0:
        print("not prime ")
        break
    y+=1
else:
    print("it is prime")
