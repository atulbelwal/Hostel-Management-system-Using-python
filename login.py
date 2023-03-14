from cgitb import text
from distutils.cmd import Command
from telnetlib import STATUS
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter import messagebox


from complaintListing import ComplaintListing
from configdb import ConnectionDatabase, new

 
from tkinter import *
import os

from status import statuslist

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

ButtonList2 = Button(root, text='Complain list2')
ButtonList2.grid(row=8, column=1)


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

    checklist = [firstname.get(), lastname.get(), room_no.get(), GenderGroup.get(),comment.get(1.0, 'end')]
    for i in checklist:
        if i == "":
            messagebox.showerror('error', 'All the fields are not filled')
            return "Wrong Entry"
        
    message = conn.Add(firstname.get(), lastname.get(), room_no.get(), GenderGroup.get(),comment.get(1.0, 'end'))
    firstname.delete(0,'end')
    lastname.delete(0, 'end')
    room_no.delete(0, 'end')
    
    comment.delete(1.0, 'end')
    showinfo(title='Add Information', message=message)
    

def ShowComplainList():

    listrequest = ComplaintListing()
    return ("YO")



#Admin................................................................................................................................................
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
                        conn = databse()
                        root = Tk()
                        root.geometry('600x300')
                        root.title('edit')
                        root.configure(bg='cyan')
                        labels = ['ID:']
                        Label(root, text=labels[0], font=("Times 20 italic bold")).grid(row=4 , column=0, padx=15, pady=20)
        
                        id = Entry(root, width=20, font=("Times 18"))
                        id.grid(row=4, column=2, columnspan=1)
                        labels = ['present Status']
                        Label(root, text=labels[0], font=("Times 20 italic bold")).grid(row=8, column=0, padx=15, pady=20)
        
                        Status = Entry(root, width=20, font=("Times 18"))
                        Status.grid(row=8, column=2, columnspan=1)
                        ButtonSubmit = Button(root, text='Submit')
                        ButtonSubmit.grid(row=10, column=2)

                        
                        def SaveStatus():

                            checklist = [id.get(), Status.get()]
                            for i in checklist:
                                if i == "":
                                    messagebox.showerror('error', 'All the fields are not filled')
                                    return "Wrong Entry"
        
                                    message = conn.Add(id.get(), Status.get())
                                    id.delete(0, 'end')
                                    Status.delete(0,'end')
                                    
                                    showinfo(title='Add Information', message=message)
    

                        def ShowComplainList2():

                            listrequest = statuslist()
                            return ("YO")
                        ButtonSubmit.config(command=SaveStatus)
                        ButtonList2.config(command=ShowComplainList2)   
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
