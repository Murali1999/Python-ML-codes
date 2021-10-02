a=''
b=''
c=int(input("Enter any number - "))

for i in range(c):
    if(i%2==0):
        a+=str(i)
    else:
        b+=str(i)


print("Even numbers - ")
print(a+" ")
print("Odd numbers - ")
print(b+" ")
