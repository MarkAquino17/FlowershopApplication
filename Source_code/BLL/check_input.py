from PyQt4 import QtCore, QtGui
import sys#bll create
import sqlite3
import os
fullpath=os.path.join(os.pardir,'DAL')
sys.path.append(fullpath)
from create_user import CreateUser
class CheckCreateInput(object):
 def SaveUser(user,password,name,fName,mName,lName,contact,address,createWindow):
    
    
    if fName=="" or mName=="" or lName=="" or user=="" or password=="" or address=="" or contact=="":
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Place make sure that all fields have been filled.")
            msg.setWindowTitle("Error")  
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            retval = msg.exec_()
            return
    
    try:
        val=int(contact)
    except ValueError:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Not a valid contact number")
            msg.setWindowTitle("Error")  
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            retval = msg.exec_()
            return
      #DAL statement?
    
    dup=CreateUser.CheckUsername(user)
      #check if the username is already in the databse
    if dup==True:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("There is already an existing username")
            msg.setWindowTitle("Duplicate")  
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            retval = msg.exec_()
    else:  
            CreateUser.InsertNewUser(user,password,name,contact,address)
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("The account has been successfully created.")
            msg.setWindowTitle("Success!!!")  
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            retval = msg.exec_()
            createWindow.close()

     
 
