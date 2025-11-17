print("********* armstrong number  ***********")

num = input("Enter any number : ")


total = 0
for digit in num:
    total += int(digit)**3

if int(num)==total:
    print("it is an armtrong number ")
else:
    print("it is not an armstrong number ")
