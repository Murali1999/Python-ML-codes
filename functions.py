#add, sub, mul, div and mod functions
#palindrome, addom, odd, even functions
#login and signup functions
#header files in c, c++..etc are modules in python

def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)
    
def mul(a,b):
    print(a*b)
    
def div(a,b):
    print(a/b)
    
def modd(a,b):
    print(a%b)

def odd(a):
    if(a%2==1):
        print(a,"is an odd number")
    else:
        print(a,"is not an odd number")

def even(a):
    if(a%2==0):
        print(a,"is an even number")
    else:
        print(a,"is not an even number")

def palindrome():
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

def addom():
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

def login():
    global u
    global p
    u = input("Enter username - ")
    p = input("Enter password - ")

    fa=open('users.txt','r')
    global f
    f=fa.read().splitlines()
    fb=open('pass.txt','r')
    global g
    g=fb.read().splitlines()

    if(u in f):
        if(p in g and f.index(u)==g.index(p)):
            print("Login successful!")
        else:
            print("Credentials are wrong")
    else:
        print("username is wrong")

    fb.close()
    fa.close()

def signup():
    global fa
    global fb
    global f, u
    global g, p
    fa = open('users.txt', 'a')
    fb = open('pass.txt', 'a')
    
    u = input("Enter username - ")
    p = input("Enter password - ")
    pp = input("Enter password again - ")

    if(p==pp and len(u)>4):
        fa.write("\n")
        fa.write(u)
        fa.write("\n")
        fb.write("\n")
        fb.write(p)
        fb.write("\n")
        print("You have signed up! Congratulations!")
    elif(p!=pp):
        print("passwords do not match!")
    elif(len(u)<4):
        print("username is short")
    else:
        print("Credentials are wrong!")

    fb.close()
    fa.close()
