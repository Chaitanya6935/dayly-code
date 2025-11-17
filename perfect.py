print("******* perfect number *************")

num1 = int(input("Enter any number "))
total = 0
for i in range(1,num1//2+1):
    if num1%i==0:
        total += i  
    print(i) 

if total == num1:
    print("it is perfect number ") 
else:
    print("it is not perfect number ")

