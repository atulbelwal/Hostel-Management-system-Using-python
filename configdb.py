
import sqlite3

class ConnectionDatabase:
	def __init__(self):
		self._db = sqlite3.connect('new2.db')
		self._db.row_factory = sqlite3.Row
		self._db.execute('create table if not exists complainTable(ID integer primary key autoincrement, FirstName varchar(255), LastName varchar(255), room_no Text, Gender varchar(255),Comment text)')
		self._db.commit()
	def Add(self,firstname,lastname,room_no, Gender,comment):
		self._db.execute('insert into complainTable (FirstName, LastName, room_no, Gender, Comment) values (?,?,?,?,?)', (firstname, lastname, room_no, Gender, comment))
		self._db.commit()
		return 'Submitted'
	def ListRequest(self):
		cursor = self._db.execute('select * from complainTable')
		return cursor

class new:
	def __init__(self):
		self._db = sqlite3.connect('new.db')
		self._db.row_factory = sqlite3.Row
		self._db.execute('create table if not exists StatusTable(ID integer  , Status varchar(255)')
		self._db.commit()
	def Add(self,id,Status):
		self._db.execute('insert into StatusTable (ID,Status) values (?,?)', (id,Status))
		self._db.commit()
		return 'Submitted'
	def ListRequest2(self):
		cursor = self._db.execute('select * from StatusTable')
		return cursor