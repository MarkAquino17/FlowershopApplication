from PyQt5 import QtCore, QtGui, QtWidgets
import sys #bll main buttons

import sqlite3

import os



fullpath=os.path.join(os.pardir,'DAL')
sys.path.append(fullpath)
from searchdatabase import Search


class ButtonControl(object):
 def loadData():
   data,connection,cursor=Search.loadDatabase()
   return (data, connection, cursor)
 def searchButton(search=None):
   result, connection, cursor =Search.searchDatabase(search)
   return (result, connection, cursor)
 def aboutButton():
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("Online flowershop service")
        msg.setInformativeText(" Coe125-C1 \n\n Created by:\n Aquino, Mark\n Chua, Cyrille Lan\n Hubalde,Angelo \n Martinez, Rain") 
        msg.setWindowTitle("About")
        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        
	
        retval = msg.exec_()
 def helpButton():
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("Instructions")
        msg.setInformativeText( '-To see all of the available items, use the "load" button. \n-Use the < and > buttons to get or remove items from the cart. \n-A "search" button is available to look for specific items.\n-Use the "reset" button to quickly empty the cart. \n-Use the "purchase" button to confirm your purchase.') 
        msg.setWindowTitle("Help")
        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        
        
	
        retval = msg.exec_()
 
 def purchaseButton(price,userID,itemID):
           Search.insertDatabase(price,userID,itemID)


          

 def checkCart(empty,price,userID,itemID):
     if empty==True:
          msg = QtWidgets.QMessageBox()
          msg.setIcon(QtWidgets.QMessageBox.Information)

          msg.setText("There must be at least a single item in the cart first.")
        
          msg.setWindowTitle("Error")
        
          msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        
	
          retval = msg.exec_()
     else :
          msg = QtWidgets.QMessageBox()
          msg.setIcon(QtWidgets.QMessageBox.Information)

          msg.setText("Are you done purchasing?")
        
          msg.setWindowTitle("Confirmation")
        
          msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        
	
          retval = msg.exec_()
          print(retval)
          if retval==1024:
            ButtonControl.purchaseButton(price,userID,itemID)
            return False
          return True
 def itemID(item,quantity):
         itemID=Search.getItemID(item)
         Search.updateItem(item,quantity)
         itemID=itemID+","+quantity+":"
         return itemID
 
 def lessThanError(value):
        if value==1:
          msg = QtWidgets.QMessageBox()
          msg.setIcon(QtWidgets.QMessageBox.Information)

          msg.setText("There are currently no available stock of this item.")
        
          msg.setWindowTitle("Error")
        
          msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        
	
          msg.exec_()


        else:
          msg = QtWidgets.QMessageBox()
          msg.setIcon(QtWidgets.QMessageBox.Information)

          msg.setText("You cannot exceed the amount available in the stock.")
        
          msg.setWindowTitle("Error")
        
          msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        
	
          msg.exec_()






     
