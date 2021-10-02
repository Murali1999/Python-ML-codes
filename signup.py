#login and sign up

ch=0
while(ch<4):
    print("1. SIGN UP")
    print("2. LOGIN")
    print("3. EXIT")
    global list1
    global list2
    list1=[]
    list2=[]
    ch=int(input("Enter the no. of what you want to do - "))

    if(ch==1):
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

        print(list1)
        print(list2)

    elif(ch==2):
        print("LOGIN")
        a = input("Enter username - ")
        b = input("Enter password - ")

        if(a in list1):
                if(b in list2 and list1.index(a)==list2.index(b)):
                   print("Login Successful!")
                   print(list1)
                   print(list2)
        
        else:
            print("Invalid Credentials! Login again!")

        print(list1)
        print(list2)
    elif(ch==3):
        print("What do you want to do?")

else:
    print("Invalid choice!")
