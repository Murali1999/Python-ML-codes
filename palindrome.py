#check palindrome number

a = input("Enter any number - ")
b = ''
b = a[::-1]
rev, num= 0,0

print("Reverse - ", b)
num = int(a)
rev = int(b)
if(rev==num):
    print("Palindrome number")
else:
    print("Not a palindrome number")


    
