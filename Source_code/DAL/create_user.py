from PyQt4 import QtCore, QtGui
import sys#dal create
import sqlite3
class CreateUser(object):
 def CheckUsername(username=None):
     connection = sqlite3.connect('ShopDatabase.db')
     cursor = connection.cursor()
     getInfo=connection.execute('SELECT Username FROM Users WHERE Username=?',[username]).fetchall()
     if not getInfo:
          dup=False
     else:
          dup=True
     cursor.close()
     connection.close()
     return dup
    
 def InsertNewUser(user=None,password=None,name=None,contact=None,address=None):
     connection = sqlite3.connect('ShopDatabase.db')
     cursor = connection.cursor()
     cursor.execute("INSERT INTO Users (Username, Password, Name,ContactNo,Address)VALUES(?,?,?,?,?)",(user,password,name,contact,address))
     connection.commit()  #save
     cursor.close()
     connection.close()
      

