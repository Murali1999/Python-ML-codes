t = int(input("Test cases: "))
for _ in range(t):
    n = int(input("Array size: "))
    a = int(input("Array elements separated by space: "))
ar=[]
ar=[int(i) for i in str(a)]
c1=ar[:(len(ar)//2)]
c2=ar[(len(ar)//2):]
print(c1)
print(c2)

count1=
