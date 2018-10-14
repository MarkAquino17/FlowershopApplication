# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
import os
import sys

path=os.path.dirname(__file__)
fullpath=os.path.join(path,'BLL')
sys.path.append(fullpath)
sys.path.append('DAL')

from check_input import CheckCreateInput
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NewUser(object):
    def __init__ (self,createWindow=None):
        self.createWindow=createWindow
    def setupUi(self, NewUser):
        NewUser.setObjectName(_fromUtf8("NewUser"))
        NewUser.resize(467, 444)

        
        NewUser.setEnabled(True)

        
        self.centralwidget = QtGui.QWidget(NewUser)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_fn = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.label_fn.setFont(font)
        self.label_fn.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fn.setObjectName(_fromUtf8("label_fn"))
        self.gridLayout.addWidget(self.label_fn, 0, 0, 1, 1)
        self.lineEdit_First = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_First.setObjectName(_fromUtf8("lineEdit_First"))
        self.gridLayout.addWidget(self.lineEdit_First, 0, 1, 1, 1)
        self.label_Mn = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.label_Mn.setFont(font)
        self.label_Mn.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Mn.setObjectName(_fromUtf8("label_Mn"))
        self.gridLayout.addWidget(self.label_Mn, 1, 0, 1, 1)
        self.lineEdit_Middle = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Middle.setObjectName(_fromUtf8("lineEdit_Middle"))
        self.gridLayout.addWidget(self.lineEdit_Middle, 1, 1, 1, 1)
        self.label_LN = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.label_LN.setFont(font)
        self.label_LN.setAlignment(QtCore.Qt.AlignCenter)
        self.label_LN.setObjectName(_fromUtf8("label_LN"))
        self.gridLayout.addWidget(self.label_LN, 2, 0, 1, 1)
        self.lineEdit_Last = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Last.setObjectName(_fromUtf8("lineEdit_Last"))
        self.gridLayout.addWidget(self.lineEdit_Last, 2, 1, 1, 1)
        self.label_user = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.label_user.setFont(font)
        self.label_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user.setObjectName(_fromUtf8("label_user"))
        self.gridLayout.addWidget(self.label_user, 3, 0, 1, 1)
        self.lineEdit_User = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_User.setObjectName(_fromUtf8("lineEdit_User"))
        self.gridLayout.addWidget(self.lineEdit_User, 3, 1, 1, 1)
        self.label_pass = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.label_pass.setFont(font)
        self.label_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pass.setObjectName(_fromUtf8("label_pass"))
        self.gridLayout.addWidget(self.label_pass, 4, 0, 1, 1)
        self.lineEdit_Pass = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Pass.setObjectName(_fromUtf8("lineEdit_Pass"))
        self.gridLayout.addWidget(self.lineEdit_Pass, 4, 1, 1, 1)
        self.label_address = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_address.sizePolicy().hasHeightForWidth())
        self.label_address.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.label_address.setFont(font)
        self.label_address.setAlignment(QtCore.Qt.AlignCenter)
        self.label_address.setObjectName(_fromUtf8("label_address"))
        self.gridLayout.addWidget(self.label_address, 5, 0, 1, 1)
        self.lineEdit_Address = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Address.setObjectName(_fromUtf8("lineEdit_Address"))
        self.gridLayout.addWidget(self.lineEdit_Address, 5, 1, 1, 1)
        self.label_contact = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_contact.sizePolicy().hasHeightForWidth())
        self.label_contact.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.label_contact.setFont(font)
        self.label_contact.setAlignment(QtCore.Qt.AlignCenter)
        self.label_contact.setObjectName(_fromUtf8("label_contact"))
        self.gridLayout.addWidget(self.label_contact, 6, 0, 1, 1)
        self.lineEdit_Contact = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Contact.setObjectName(_fromUtf8("lineEdit_Contact"))
        self.gridLayout.addWidget(self.lineEdit_Contact, 6, 1, 1, 1)
        self.btn_create = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_create.sizePolicy().hasHeightForWidth())
        self.btn_create.setSizePolicy(sizePolicy)
        self.btn_create.setObjectName(_fromUtf8("btn_create"))
        self.gridLayout.addWidget(self.btn_create, 7, 1, 1, 1)
        NewUser.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(NewUser)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        NewUser.setStatusBar(self.statusbar)

        self.retranslateUi(NewUser)
        QtCore.QMetaObject.connectSlotsByName(NewUser)
        NewUser.setStyleSheet("#NewUser { border-image: url(flower_pink.jpg) 0 0 0 0 stretch stretch; }")
        self.btn_create.clicked.connect(self.on_pushButton_clicked_create)
        #self.btn_create.setFlat(True)
        #self.btn_create.setAutoFillBackground(True)

        ####
##        self.btn_create.setStyleSheet("QPushButton { background-image: url(Yamcha_Missing_Tooth_LOL.jpg)0 0 0 0 stretch stretch ; }")
##        self.btn_create.setIcon(QtGui.QIcon("Yamcha_Missing_Tooth_LOL.jpg"))
##        self.btn_create.setIconSize(QtCore.QSize(100,100))
        ####

        
    def retranslateUi(self, NewUser):
        NewUser.setWindowTitle(_translate("NewUser", "Create Account", None))
        self.label_fn.setText(_translate("NewUser", "First Name", None))
        self.label_Mn.setText(_translate("NewUser", "Middle Name", None))
        self.label_LN.setText(_translate("NewUser", "Last Name", None))
        self.label_user.setText(_translate("NewUser", "Username", None))
        self.label_pass.setText(_translate("NewUser", "Password", None))
        self.label_address.setText(_translate("NewUser", "Address", None))
        self.label_contact.setText(_translate("NewUser", "Contact Number", None))
        self.btn_create.setText(_translate("NewUser", "create account", None))

    def on_pushButton_clicked_create(self):
        
        
        self.fName=self.lineEdit_First.text()
        self.mName=self.lineEdit_Middle.text()
        self.lName=self.lineEdit_Last.text()
        self.user=self.lineEdit_User.text()
        self.password=self.lineEdit_Pass.text()
        self.address=self.lineEdit_Address.text()
        self.contact=self.lineEdit_Contact.text()
        self.Name=self.lName+", "+self.fName+", "+self.mName
        CheckCreateInput.SaveUser(self.user,self.password,self.Name,self.fName,self.mName,self.lName,self.contact,self.address,self.createWindow)
        
        


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    NewUser = QtGui.QMainWindow()
    ui = Ui_NewUser()
    ui.setupUi(NewUser)
    NewUser.show()
    sys.exit(app.exec_())

