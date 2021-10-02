a = int(input("Enter a number - "))
print("Number -",a)

sq = (a*a)
b=str(sq)
print("Square of number -",sq)

c=b[::-1]
print("Reverse of square -",c)

d = int(c)
e = int(d**0.5)
print("Square root of reverse number -",e)
sqrev = str(e)

f = sqrev[::-1]
rev = int(f)
print("Reverse of square root -",rev)

if(rev==a):
    print("This number is an Addom number")
else:
    print("This number is not an Addom number")
