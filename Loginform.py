from tkinter import *
import tkinter.messagebox as MessageBox
root=Tk()
root.title("Login Page")
root.geometry("500x500")
root.configure(bg="blue")
def validate():
    uname1=t_uname.get()
    pwd1=t_pwd.get()
    if uname1=="abc@gmail.com" and pwd1=="secret":
        MessageBox.showinfo(uname1, "Administratar Logging Successfully")
    elif uname1=="abcd@gmail.com" and pwd1=="secret":
        MessageBox.showinfo(uname1,"Non Administrator Logging Successfully")
    else:
        MessageBox.showinfo(uname1,"Wrong Credentials")
   
#Label for title creation
title=Label(root,text="Login Form",fg="white",bg="blue",font=("bold",15))
title.place(x=220,y=30)
#Label for username creation
uname=Label(root,text="Username",fg="white",bg="blue",font=("bold",15))
uname.place(x=80,y=80)
#Label for password creation
pwd=Label(root,text="Password",fg="white",bg="blue",font=("bold",15))
pwd.place(x=80,y=120)
#Button for submit
submit=Button(root,text="Submit",fg="white",bg="blue",font=("bold",15),comman=validate)
submit.place(x=200,y=160)
#Entry field creation for username
t_uname=Entry()
t_uname.place(x=200,y=87)
#Entry field creation for password
t_pwd=Entry()
t_pwd.place(x=200,y=127)
root.mainloop()