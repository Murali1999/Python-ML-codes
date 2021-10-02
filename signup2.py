#functions for login and sign up

global list1
global list2
ch=0
list1,list2=[],[]

def signup():
    print("SIGN UP")
    a = input("Enter username - ")
    b = input("Enter password - ")
    c = input("Re-enter password - ")

    if(len(a)<4):
        print("Username length too small!")
    else:
        list1.append(a)

    if(b==c):
        list2.append(b)
    else:
        print("Passwords do not match! Sign up again.")
        list1.clear()
        list2.clear()

    print(list1)
    print(list2)

def login():
    print("LOGIN")
    a = input("Enter username - ")
    b = input("Enter password - ")

    if(a in list1):
            if(b in list2 and list1.index(a)==list2.index(b)):
                print("Login Successful!")
    else:
        print("Invalid Credentials! Login again!")

while(ch<=4):
    
    print("1. SIGNUP")
    print("2. LOGIN")
    print("3. EXIT")

    ch=int(input("Enter choice - "))

    if(ch==1):
        signup()
    elif(ch==2):
        login()
    elif(ch==3):
        input("Press enter to exit")
        break

else:
    print("Invalid choice")
