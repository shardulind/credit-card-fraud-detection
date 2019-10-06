import tkinter as tk
from tkinter import *
from tkinter import messagebox
import users
import transactions
login_attempt = 0;



# this function runs after successful login

def start_payment_window():

    def validate():
        if ccnumber.get() == '':
            messagebox.showinfo('Incomplete Form','Enter Credit Card Number')
            return False

        elif amount.get() == '':
            messagebox.showinfo('Incomplete Form','Enter Amount')
            return False

        elif country.get() == '':
            messagebox.showinfo('Incomplete Form','Enter Country')
            return False
        else:
            return True


    #this starts on clicking pay button
    def start_payment():
        flag = validate()   #validation to check if form is completly filled or not
                            #flag = true means form is correctly filled
        if flag == True:
            #checking if transaction is fraud or not by calling
            # is_unusual_payment function from transaction.py module

            check = transactions.is_unusual_payment(ccnumber.get(),amount.get(),country.get())

            #if yes the Fraud detected
            if check == True:
                messagebox.showerror('',"Fraud Detected")
                payment_win.destroy()

            #else no fraud detected
            else:
                #adding transaction in transaction.csv
                transactions.add_transaction_detail(ccnumber.get(), amount.get(), country.get())
                messagebox.showinfo("Success","Transaction Completed")
                payment_win.destroy()

        #if form is not filled properly
        elif flag == False:
            return


    # payment window
    payment_win = tk.Tk()
    payment_win.title("Online Credit Card Payment ")
    payment_win.geometry("350x400+750+300")

    Label(payment_win, text="Online Transaction").grid(row=0, column=4)
    Label(payment_win, text="Credit Card Number: ").grid(row=1,column=3)
    Label(payment_win, text="Amount: ").grid(row=2,column=3)
    Label(payment_win, text="Country: ").grid(row=3,column=3)

    ccnumber = Entry(payment_win)
    amount = Entry(payment_win)
    country = Entry(payment_win)

    ccnumber.grid(row=1,column=4)
    amount.grid(row=2,column=4)
    country.grid(row=3,column=4)

    Button(payment_win, text="Pay", command=start_payment).grid(row=5, column=3)
    Button(payment_win, text="Cancle", command=payment_win.destroy).grid(row=5, column=4)
    mainloop()



#function starts on clicking on login button
def start_login():

    #this function runs after clicking login button
    def login():

            #to count number of login attempts
            global login_attempt
            login_attempt +=1

            #checking users login by calling login function from users.py
            check = users.user_login(username.get(), password.get())

            #check=true means user_login successful
            if check == True:
                # logged in transit to next payment window
                login_attempt=0
                login_win.destroy()
                start_payment_window()

            # if login is tried for 3 times then some fraud is detected
            elif login_attempt==3:
                #fraud detected.. 3 login attempts done
                messagebox.showerror("","Fraud Detected: Multiple failed Login attempts")
                login_win.destroy()
            else:
                messagebox.showerror("","Wrong Username or password")



    #login window
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



#this function starts after clicking register button
def start_user_reg():
    reg_win = tk.Tk()
    reg_win.title("User Registration")
    reg_win.geometry('450x400+750+600')

    def validate():
        if name.get() == '':
            messagebox.showinfo('Validation Error','Name field is Empty')
            return False

        elif ccnumber.get() == '':
            messagebox.showinfo('Validation Error','Enter Credit Card Number')
            return False

        elif mno.get() == '':
            messagebox.showinfo('Validation Error','Enter Mobile Number')
            return False

        elif email.get() == '':
            messagebox.showinfo('Validation Error','Enter email id')
            return False

        elif country.get() =='':
            messagebox.showinfo('Validation Error','Enter county ')
            return False

        elif username.get() == '':
            messagebox.showinfo('Validation Error','Enter Username')
            return False

        elif password.get() == '':
            messagebox.showinfo('Validation Error','Enter password')
            return False
        else:
            return True


    #this function starts on clicking register button
    def register_user():
        #validation checking if all details are filled correctly
        flag = validate()

        #flag = true means form filled correctly
        if flag == True:
            #adding users
            users.add_new_user(name.get(),ccnumber.get(), mno.get(), email.get(), country.get(), username.get(), password.get())
            reg_win.destroy()
        elif flag == False:
            return

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



# driver Program

main_win = tk.Tk()
main_win.title("Credit Card Transaction Fraud Detection System")
main_win.geometry("600x600")


l = Label(main_win, font=('arial',15), relief = "groove", text="Credit Card Services")
l.grid(row=0, column=8, padx=50, pady=10)
reg = Button(main_win, text="Register", command=start_user_reg)
log = Button(main_win, text="Login", command=start_login)
exit = Button(main_win, text="Exit", command=exit)

reg.grid(row=5, column=3, pady=10, padx=10)
log.grid(row=6, column=3, pady=10, padx=10)
exit.grid(row=7, column=3, pady=10, padx=10)

mainloop()
