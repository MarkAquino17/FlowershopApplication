from PyQt4 import QtCore, QtGui
import sys #bll login and main userinfo
import sqlite3
import os
fullpath=os.path.join(os.pardir,'DAL')
sys.path.append(fullpath)
from searchdatabase import Search

class GetUserInfo(object):
 def __init__(self,username,password):
     self.username=username
     self.password=password
     self.valid=self.checkInfo()
     if self.valid==True:
      self.user=Search.getInfo(self.username,self.password)
     
      self.UserID=self.user[0][0]
      self.Name=self.user[0][1]
      self.Contact=self.user[0][2]
      self.Address=self.user[0][3]
 def checkValid(self):
     return self.valid
 def checkInfo(self):
      #DAL statement?
      valid=Search.CheckInfo(self.username,self.password)
      #check if the username is already in the databse
      if valid==True:
             return True
      else:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("The supplied username or password is not correct")
            msg.setWindowTitle("Wrong info")  
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            retval = msg.exec_()

 def getUser(self):

     return self.user
 
 def accountInfo(self):
     msg = QtGui.QMessageBox()
     msg.setIcon(QtGui.QMessageBox.Information)

     msg.setText("Name: "+self.Name)
     msg.setInformativeText("Username: "+self.username+"\n User ID: "+str(self.UserID)+"\n Contact: "+str(self.Contact)+"\n Address: "+self.Address)
     msg.setWindowTitle("Account Details")  
     msg.setStandardButtons(QtGui.QMessageBox.Ok)
     retval = msg.exec_()
