#program to ask user what he/she wishes to do

import functions
from functions import *
global ask
ask=0
global f, g, u, p
print("List of functions in the module - ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Palindrome")
print("7. Addom")
print("8. Odd")
print("9. Even")
print("10. Login")
print("11. Sign-Up")
print("(0 to exit)")
while(ask<12):
    ask = int(input("What do you want to do? "))
    
    if(ask==1):
        print("Addition")
        a = int(input("number 1 - "))
        b = int(input("number 2 - "))
        add(a,b)
    elif(ask==2):
        print("Subtraction")
        a = int(input("number 1 - "))
        b = int(input("number 2 - "))
        sub(a,b)
    elif(ask==3):
        print("Multiplication")
        a = int(input("number 1 - "))
        b = int(input("number 2 - "))
        mul(a,b)
    elif(ask==4):
        print("Division")
        a = int(input("number 1 - "))
        b = int(input("number 2 - "))
        div(a,b)
    elif(ask==5):
        print("Modulus")
        a = int(input("number 1 - "))
        b = int(input("number 2 - "))
        mod(a,b)
    elif(ask==6):
        print("Palindrome number")
        palin()
    elif(ask==7):
        print("Addom number")
        addom()
    elif(ask==8):
        print("Odd number")
        a = int(input("number - "))
        odd(a)
    elif(ask==9):
        print("Even number")
        a = int(input("number - "))
        even(a)
    elif(ask==10):
        print("Login page")
        login()
    elif(ask==11):
        print("Sign-up page")
        signup()
    elif(ask==0):
        print("Do you want to exit?")
        input("Press enter to exit")
else:
    print("Invalid choice!")
