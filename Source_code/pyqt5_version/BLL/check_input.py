from PyQt5 import QtCore, QtGui, QtWidgets
import sys#bll create

import sqlite3

import os

fullpath=os.path.join(os.pardir,'DAL')
sys.path.append(fullpath)
from create_user import CreateUser

class CheckCreateInput(object):
 def SaveUser(user,password,name,fName,mName,lName,contact,address,createWindow):
    
    
    if fName=="" or mName=="" or lName=="" or user=="" or password=="" or address=="" or contact=="":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Place make sure that all fields have been filled.")
            msg.setWindowTitle("Error")  
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
            return
    
    try:
        val=int(contact)
    except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Not a valid contact number")
            msg.setWindowTitle("Error")  
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
            return
      #DAL statement?
    
    dup=CreateUser.CheckUsername(user)
      #check if the username is already in the databse
    if dup==True:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("There is already an existing username")
            msg.setWindowTitle("Duplicate")  
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
    else:  
            CreateUser.InsertNewUser(user,password,name,contact,address)
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("The account has been successfully created.")
            msg.setWindowTitle("Success!!!")  
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
            createWindow.close()

     
 
