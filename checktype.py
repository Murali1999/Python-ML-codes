#check if number entered is odd, even, addom or palindrome number

x=int(input("Enter number - "))
print("Number -",x)

for a in range(0,x):
    def palin(a):
        b=''
        b=str(a)
        c=[]
        c=[int(b[::-1])]
        return c

    def addom(a):
        sqr=0
        sqr=(a*a)
        c=''
        c=str(sqr)
        d=int(c[::-1])
        e=int(d**0.5)
        f=str(e)
        r=''
        r=f[::-1]
        rev=[]
        rev=[int(r)]
        return rev

global num
num=[]
num=palin(x)
global nums
nums=[]
nums=addom(x)

global list1
global list2
global list3
global list4
list1,list2,list3,list4=[],[],[],[]
global dictofnumbers
dictofnumbers={'odd':list1, 'even':list2, 'addom':list3, 'palin':list4}

if(x%2==0):
    print("Number is even")
    list2=[x]
    if(num==x):
        print("its a palindrome number")
        list4=[x]
    elif(nums==x):
        print("its an addom number")
        list3=[x]
    else:
        print("none of these")
elif(x%2==1):
    print("Number is odd")
    list1=[x]
    if(num==x):
        print("its a palindrome number")
        list4=[x]
    elif(nums==x):
        print("its an addom number")
        list3=[x]
    else:
        print("none of these")

dictofnumbers={'odd':list1, 'even':list2, 'addom':list3, 'palin':list4}
print(dictofnumbers)
