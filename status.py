from tkinter import *
from tkinter.ttk import *
import sqlite3

from configdb import ConnectionDatabase

class statuslist:
    def __init__(self):
        self.connectionDB = ConnectionDatabase()
        self.connectionDB.row_factory = sqlite3.Row
        self.root = Tk()
        self.root.title('Complaint Status')
        tree = Treeview(self.root)
        tree.pack()
        tree.heading('#id', text='ID')
        tree.configure(column=('#id','#Status'))
        tree.heading('#FirstName', text='First Name')
        
        tree.column('#0', stretch=NO, minwidth=0, width=100)
        tree.column('#1', stretch=NO, minwidth=0, width=100)
    
        cursor = self.connectionDB.ListRequest()
        for row in cursor:
            tree.insert('#{}'.format(row['ID']), text=row['ID'])
            tree.set('#{}'.format(row['ID']), '#Status', row['Status'])