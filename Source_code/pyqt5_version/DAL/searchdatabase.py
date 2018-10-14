from PyQt5 import QtCore
import sys#dal login and main user get

import sqlite3

import datetime

class Search(object):
 def CheckInfo(user,password):
        connection = sqlite3.connect('ShopDatabase.db')
        cursor = connection.cursor()
        getInfo=connection.execute('SELECT Username,Password FROM Users WHERE Username=? AND Password=?',[user,password]).fetchall()
        
        if not getInfo: #check if the list is empty, if it is empty the input pass and user is wrong        
            valid=False
        else:
            valid=True
        cursor.close()
        connection.close()
        return valid
    
 def getInfo(username,password):
    connection = sqlite3.connect('ShopDatabase.db')
    cursor=connection.cursor()
    getUser=connection.execute('SELECT UserID,Name,ContactNo,Address FROM Users WHERE Username=? AND Password=?',[username,password]).fetchall()
    cursor.close()
    connection.close()
    return getUser

 def loadDatabase():
     connection = sqlite3.connect('ShopDatabase.db')
        
     query = "SELECT ItemName,Quantity,ItemPrice FROM Stock"
     cursor=connection.cursor()
     result = connection.execute(query)

     return (result, connection, cursor)


 def searchDatabase(search=None):
     connection = sqlite3.connect('ShopDatabase.db')
     cursor=connection.cursor()
     result=connection.execute("SELECT ItemName,Quantity,ItemPrice FROM Stock WHERE ItemName LIKE ?",('%'+search+'%',))

     return (result, connection, cursor)
 def insertDatabase(price,userID,itemID):
     connection = sqlite3.connect('ShopDatabase.db')
     cursor=connection.cursor()
     now = datetime.datetime.now()
     time=now.strftime("%Y-%m-%d %H:%M")
     cursor.execute("INSERT INTO Purchase (UserID,ItemID,OrderDate,Bill) VALUES (?,?,?,?)",(userID,itemID,time,price))
     connection.commit()
     cursor.close()
     connection.close()
 def getItemID(search=None):
     connection = sqlite3.connect('ShopDatabase.db')
     cursor=connection.cursor()
     result=connection.execute('SELECT ItemID FROM Stock WHERE ItemName=?',[search]).fetchall()
     itemID=str(result[0][0])
     cursor.close()
     connection.close()
     return itemID
 def updateItem(item,quantity):
     connection = sqlite3.connect('ShopDatabase.db')
     cursor=connection.cursor()
     result=connection.execute('SELECT Quantity FROM Stock WHERE ItemName=?',[item]).fetchall()
     newQuantity=result[0][0]-int(quantity)
     connection.execute('UPDATE Stock SET Quantity =? WHERE ItemName=?',[newQuantity,item])
     connection.commit()
     cursor.close()
     connection.close()
     return 



     
