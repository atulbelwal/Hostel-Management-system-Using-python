
from cgitb import text
from distutils.cmd import Command
from telnetlib import STATUS
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter import messagebox


from complaintListing import ComplaintListing
from configdb import ConnectionDatabase

 
from tkinter import *
import os
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="Continue", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
    main_screen.destroy()
    #login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
 
#Config


conn = ConnectionDatabase()
root = Tk()
root.geometry('720x600')
root.title('Residential Society Complaint Management System')
root.configure(bg='cyan')

#Style

style = Style()
style.theme_use('classic')



labels = ['First Name:', 'Last Name:', 'Room_no:', 'Gender:', 'Complain:']
for i in range(5):
    Label(root, text=labels[i], font=("Times 20 italic bold")).grid(row=i, column=0, padx=15, pady=20)
    
ButtonList = Button(root, text='Complain list')
ButtonList.grid(row=5, column=1)

ButtonSubmit = Button(root, text='Submit')
ButtonSubmit.grid(row=5, column=2)

ButtonAdmin = Button(root, text='Admin')
ButtonAdmin.grid(row=5, column=0)

# Entries
firstname = Entry(root, width=40, font=("Times 18"))
firstname.grid(row=0, column=1, columnspan=2)

lastname = Entry(root, width=40, font=("Times 18"))
lastname.grid(row=1, column=1, columnspan=2)

room_no = Entry(root, width=40, font=("Times 18"))
room_no.grid(row=2, column=1, columnspan=2)

GenderGroup = StringVar()
Radiobutton(root, text='Male', value='male', variable=GenderGroup).grid(row=3, column=1)
Radiobutton(root, text='Female', value='female', variable=GenderGroup).grid(row=3, column=2)



comment = Text(root, width=40, height=6, font=('Cambria', 14))
comment.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
Status="pending"
def SaveData():

    checklist = [firstname.get(), lastname.get(), room_no.get(), GenderGroup.get(), Status.get(),comment.get(1.0, 'end')]
    for i in checklist:
        if i == "":
            messagebox.showerror('error', 'All the fields are not filled')
            return "Wrong Entry"
        
    message = conn.Add(firstname.get(), lastname.get(), room_no.get(), GenderGroup.get(),Status.get(),comment.get(1.0, 'end'))
    firstname.delete(0,'end')
    lastname.delete(0, 'end')
    room_no.delete(0, 'end')
    Status.delete(0,'end')
    comment.delete(1.0, 'end')
    showinfo(title='Add Information', message=message)
    

def ShowComplainList():

    listrequest = ComplaintListing()
    return ("YO")
def adminpassword():
       
        root = Tk()
        root.geometry('600x300')
        root.title('password')
        root.configure(bg='cyan')
        labels = ['Admin Password:']
        Label(root, text=labels[0], font=("Times 20 italic bold")).grid(row=i, column=0, padx=15, pady=20)
        
        adminpassword = Entry(root, width=20, font=("Times 18"),show='*')
        adminpassword.grid(row=4, column=2, columnspan=1)
        
        Buttonok = Button(root, text='ok')
        Buttonok.grid(row=5, column=0)
        
            
        
        def submit():
            
            
            
            if (adminpassword.get()=="atul"):
                    root = Tk()
                    root.geometry('600x300')
                    root.title('password')
                    root.configure(bg='cyan')
                    Buttonedit = Button(root, text='edit status')
                    Buttonedit.grid(row=5, column=0)
                    ButtonExit = Button(root, text='Exit')
                    ButtonExit.grid(row=5, column=4)
                    
                    
                    ButtonExit.config(command=exit)
                    def edit():
                        root = Tk()
                        root.geometry('600x300')
                        root.title('edit')
                        root.configure(bg='cyan')
                        labels = ['ID:']
                        id = Entry(root, width=20, font=("Times 18"))
                        id.grid(row=1, column=2, columnspan=2)
                        labels = ['Status']
                        
                        Status= Entry(root, width=40, font=("Times 18"))
                        Status.grid(row=3, column=2, columnspan=2)
                        
                        
                    Buttonedit.config(command=edit)
            else:
                print('ram')
    
        Buttonok.config(command=submit)
#Style

style = Style() 
style.theme_use('classic')


ButtonSubmit.config(command=SaveData)
ButtonList.config(command=ShowComplainList)
ButtonAdmin.config(command=adminpassword)

        

root.mainloop()
