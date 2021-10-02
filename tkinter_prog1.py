#login page and exit using tkinter

import tkinter as tk
from tkinter import Button
fa=open('users.txt','w')
fa.close()
fb=open('pass.txt','w')
fb.close()

un,pw=[],[]
list1,list2=[],[]
win=tk.Tk()
win.title('LOGIN PAGE')
win.geometry('300x300')
title1=tk.Label(win,text='WELCOME TO THE LOGIN PAGE')
title1.place(x=30,y=1)
lab1=tk.Label(win,text='Enter Username:')
lab1.place(x=2,y=30)
lab2=tk.Label(win,text='Enter Password:')
lab2.place(x=2,y=65)

def checkcreds():
    u=entry1.get()
    p=entry2.get()
    #global list1, list2
    #un,pw=list1,list2
    fa=open('users.txt','r')
    global f
    un=fa.read().splitlines()
    fb=open('pass.txt','r')
    global g
    pw=fb.read().splitlines()

    win2=tk.Tk()
    win2.geometry('400x400')
    exit1=Button(win2,text='Exit',command=quitnow)
    if(u in un):
        if(p in pw and un.index(u)==pw.index(p)):
            info=tk.Label(win2,text='CREDENTIALS ARE CORRECT. WELCOME USER!')
            info.place(x=20,y=40)
            exit1.place(x=20,y=70)
        elif(p not in pw):
            info=tk.Label(win2,text='PASSWORD IS WRONG')
            info.place(x=20,y=40)
            exit1.place(x=20,y=70)
    else:
        info=tk.Label(win2,text='CREDENTIALS ARE WRONG')
        info.place(x=20,y=40)
        exit1.place(x=20,y=70)

    fb.close()
    fa.close()

button1=Button(win,text='Submit',command=checkcreds)
button1.place(x=10,y=100)
entry1=tk.Entry(win)
entry1.place(x=95,y=30)
entry2=tk.Entry(win,show='*')
entry2.place(x=95,y=65)

def quitnow():
    exit()

exit1=Button(win,text='Quit',command=quitnow)
exit1.place(x=70,y=100)

def savecreds():
    a=ent1.get()
    b=ent2.get()
    c=ent3.get()
    global list1,list2
    if((a=='' and b=='') or (a=='' and c=='')):
        check=tk.Label(win3,text='YOU CANNOT LEAVE THE CREDENTIALS EMPTY!')
        check.place(x=20,y=150)
    
    if(len(a)>4):
        #list1.append(a)
        fa=open('users.txt', 'a')
        fa.write(a)
        fa.write("\n")
    else:
        check=tk.Label(win3,text='USERNAME IS SHORT.')
        check.place(x=20,y=150)
        #list1.clear()
        fa=open('users.txt', 'w')
        fa.write('')
    if(b==c):
        #list2.append(b)
        fb=open('pass.txt', 'a')
        fb.write(b)
        fb.write("\n")
    else:
        check=tk.Label(win3,text='PASSWORDS DO NOT MATCH.')
        check.place(x=20,y=150)
        #list1.clear()
        #list2.clear()
        fb=open('pass.txt', 'w')
        fb.write('')

    fb.close()
    fa.close()

#def signup():
win3=tk.Tk()
win3.title('SIGN-UP PAGE')
win3.geometry('300x300')
title1=tk.Label(win3,text='WELCOME TO THE SIGN-UP PAGE')
title1.place(x=30,y=1)
lab1=tk.Label(win3,text='Enter Username:')
lab1.place(x=2,y=35)
lab2=tk.Label(win3,text='Enter Password:')
lab2.place(x=2,y=65)
lab3=tk.Label(win3,text='Enter Again:')
lab3.place(x=2,y=95)
button1=Button(win3,text='Submit',command=savecreds)
button1.place(x=10,y=125)
ent1=tk.Entry(win3)
ent1.place(x=95,y=35)
ent2=tk.Entry(win3,show='*')
ent2.place(x=95,y=65)
ent3=tk.Entry(win3,show='*')
ent3.place(x=95,y=95)
