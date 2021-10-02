#login using files

fa=open('users.txt','w')
fa.close()
fb=open('pass.txt','w')
fb.close()

fa=open('users.txt', 'a')
fa.write('murali')
fa.write("\n")
fa.write('user1')
fa.write("\n")
fa.write('user2')

fb=open('pass.txt', 'a')
fb.write('12345')
fb.write("\n")
fb.write('abcd')
fb.write("\n")
fb.write('ab@123')

u = input("Enter username - ")
p = input("Enter password - ")

fa=open('users.txt','r')
global f
f=fa.read().splitlines()
fb=open('pass.txt','r')
global g
g=fb.read().splitlines()
print(f)
print(g)

if(u in f):
    if(p in g and f.index(u)==g.index(p)):
        print("Login successful!")
    else:
        print("Credentials are wrong")
else:
    print("username is wrong")

fb.close()
fa.close()
