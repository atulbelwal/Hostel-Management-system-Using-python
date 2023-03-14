
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter import messagebox

from complaintListing import ComplaintListing
from configdb import ConnectionDatabase

#Config
class loginak(Frame):
    def _init_(self,master):
        super()._init_(master)
        self.lable_username=Lable1(self,text="username",font=("Time of roman",15))
        self.lable_password=Lable2(self,text="Password",font=("Time of roman",15))
        
        self.entry_username=Entry(self)
        self.entry_password=Entry(self)
        self.label_username.grid(row=0,sticky=E)
        self.label_password.grid(row=1,sticky=E)
        self.entry_username.grid(row=0,column=1)
        self.entry_password.grid(row=1,column=1)
         
        self.button=Button(self,text='login',command=self.login)
        self.button.grid(columnspan=2)
        self.pack()
        
        def login(self):
            username=self.entry_username.get()
            password=self.entry_password.get()
            
            if (username=='atul' and password=='password'):
                
                mb.showinfo("login",'login successfully')
                
            else:
                mb.showinfo('login','login failed')
                
                ak=Tk()
                login=Loginak(ak)
                ak.mainloop9
                
        
        

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

def SaveData():

    checklist = [firstname.get(), lastname.get(), room_no.get(), GenderGroup.get(), comment.get(1.0, 'end')]
    for i in checklist:
        if i == "":
            messagebox.showerror('error', 'All the fields are not filled')
            return "Wrong Entry"
        
    message = conn.Add(firstname.get(), lastname.get(), room_no.get(), GenderGroup.get(), comment.get(1.0, 'end'))
    firstname.delete(0,'end')
    lastname.delete(0, 'end')
    room_no.delete(0, 'end')
    comment.delete(1.0, 'end')
    showinfo(title='Add Information', message=message)
    

def ShowComplainList():

    listrequest = ComplaintListing()
    return ("YO")


ButtonSubmit.config(command=SaveData)
ButtonList.config(command=ShowComplainList)


root.mainloop()
