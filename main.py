import tkinter as tk
from tkinter import *
from tkinter import messagebox
import users

login_attempt = 0;

def start_login():

    def login():
            global login_attempt
            login_attempt +=1
            check = users.user_login(username.get(), password.get())
            if check == True:
                # logged in transit to next Window
                login_attempt=0
                login_win.destroy()
                start_payment_window()

            elif login_attempt==3:
                #fraud detected.. 3 login attempts done
                messagebox.showerror("Fraud Detected: Multiple Login attempts")
                login_win.destroy()



    login_win = tk.Tk()
    login_win.title("Login Window")
    login_win.geometry('350x200+800+400')

    Label(login_win, text="Login for online Credit Card Transactions").grid(row=0,column=4)
    Label(login_win, text="username: ").grid(row=2,column=3)
    Label(login_win, text="password: ").grid(row=3, column=3)

    username = Entry(login_win)
    password = Entry(login_win, show="*")

    username.grid(row=2, column=4)
    password.grid(row=3, column=4)

    Button(login_win,text = "Login", command=login).grid(row=5, column=3)
    Button(login_win,text = "Cancle", command=login_win.destroy).grid(row=5, column=4)
    mainloop()


def start_user_reg():
    reg_win = tk.Tk()
    reg_win.title("User Registration")
    reg_win.geometry('450x400+750+600')


    def register_user():
        users.add_new_user(name.get(),ccnumber.get(), mno.get(), email.get(), country.get(), username.get(), password.get())

        #valid_pass = validation()
        #if valid_pass == True:
            #msg = add_new_member(member_types_array[v.get()], mno.get(), email.get(),fn.upper())
            #if member added Successfully
            #if msg == 1:
            #    messagebox.showinfo("Successful","Member added Successfully")
            #    reg_win.destroy()
            #    print("Member" + fn +" Added Successful !!!")
            #else:
            #    messagebox.showinfo('Member Already Exist',msg)
            #    reg_win.destroy()
        #else:
            #pop some error ;; pop valid_pass
            #messagebox.showinfo('Form Validation Error', valid_pass)


    Label(reg_win, text="Credit Card User Registration").grid(row=0,column=4)
    Label(reg_win, text="Name: ").grid(row=3,column=3)
    Label(reg_win, text="Credit Card Number: ").grid(row=4,column=3)
    Label(reg_win, text="Mobile Number:").grid(row=5,column=3)
    Label(reg_win, text="Email Id:").grid(row=6,column=3)
    Label(reg_win, text="Country: ").grid(row=7, column=3)
    Label(reg_win, text="username: ").grid(row=9, column=3)
    Label(reg_win, text="password: ").grid(row=10,column=3)

    name = Entry(reg_win)
    ccnumber = Entry(reg_win)
    mno = Entry(reg_win)
    email = Entry(reg_win)
    country = Entry(reg_win)
    username = Entry(reg_win)
    password = Entry(reg_win)

    name.grid(row=3,column=4)
    ccnumber.grid(row=4,column=4)
    mno.grid(row=5,column=4)
    email.grid(row=6,column=4)
    country.grid(row=7, column=4)
    username.grid(row=9, column=4)
    password.grid(row=10, column=4)


    Button(reg_win, text='Close', command=reg_win.destroy).grid(row=12,column=4, sticky=W, pady=4)
    Button(reg_win, text='Register', command=register_user).grid(row=12,column=5, sticky=W, pady=4)

    mainloop()


start_login()
