list1=['user','user1','user2','murali']
list2=['ab@123','wxyz','rhaegar','12345']

a = input("Enter username - ")
b = input("Enter password - ")

if(a in list1):
    if(b in list2):
        if(b in list2 and list1.index(a)==list2.index(b)):
           print("Login Successful!")
        else:
           print("Invalid Credentials! Login again!")


