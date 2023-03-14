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








def edit():
    editor=Tk()
    editor.geometry('600x300')
    editor.title('password')
    editor.configure(bg='cyan')
    labels = ['Admin Password:']

    editor.mainloop()
