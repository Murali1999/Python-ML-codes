#store all types of numbers in a dictionary

inp=int(input("Enter number - "))
global dict1
global li1, li2, li3, li4
li1,li2,li3,li4=[],[],[],[]
dict1={'odd':li1,'even':li2,'addom':li3,'palin':li4}

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
        rev=0
        rev=int(r)
        return rev

def palin(a):
        b=''
        b=str(a)
        c=0
        c=int(b[::-1])
        return c

for x in range(inp):
    li1=[i for i in range(x) if i%2==1]
    li2=[j for j in range(x) if j%2==0]
    li3=[k for k in range(x) if addom(k)==k]
    li4=[l for l in range(x) if palin(l)==l]
else:
    print("out of range")

print({'odd':li1,'even':li2,'addom':li3,'palin':li4})
         
    
    
    
