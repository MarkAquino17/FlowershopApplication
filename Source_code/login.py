# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import create
import main
import sqlite3
import os
import sys

path=os.path.dirname(__file__)
fullpath=os.path.join(path,'BLL')
sys.path.append(fullpath)
sys.path.append('DAL')
from Get_User import GetUserInfo
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

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName(_fromUtf8("LoginWindow"))
        LoginWindow.resize(573, 330)
        LoginWindow.setEnabled(True)
        self.centralwidget = QtGui.QWidget(LoginWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_pass = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pass.sizePolicy().hasHeightForWidth())
        self.label_pass.setSizePolicy(sizePolicy)
        self.label_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pass.setObjectName(_fromUtf8("label_pass"))
        self.gridLayout.addWidget(self.label_pass, 2, 0, 1, 1)
        self.lineEdit_Pass = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Pass.setText(_fromUtf8(""))
        self.lineEdit_Pass.setObjectName(_fromUtf8("lineEdit_Pass"))
        self.gridLayout.addWidget(self.lineEdit_Pass, 2, 1, 1, 1)
        self.btn_Signup = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Signup.sizePolicy().hasHeightForWidth())
        self.btn_Signup.setSizePolicy(sizePolicy)
        self.btn_Signup.setObjectName(_fromUtf8("btn_Signup"))
        self.gridLayout.addWidget(self.btn_Signup, 3, 0, 1, 1)
        self.btn_Login = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Login.sizePolicy().hasHeightForWidth())
        self.btn_Login.setSizePolicy(sizePolicy)
        self.btn_Login.setObjectName(_fromUtf8("btn_Login"))
        self.gridLayout.addWidget(self.btn_Login, 3, 1, 1, 1)
        self.label_user = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_user.sizePolicy().hasHeightForWidth())
        self.label_user.setSizePolicy(sizePolicy)
        self.label_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user.setObjectName(_fromUtf8("label_user"))
        self.gridLayout.addWidget(self.label_user, 1, 0, 1, 1)
        self.lineEdit_User = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_User.setText(_fromUtf8(""))
        self.lineEdit_User.setObjectName(_fromUtf8("lineEdit_User"))
        self.gridLayout.addWidget(self.lineEdit_User, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(LoginWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)
        LoginWindow.setStyleSheet("#LoginWindow { border-image: url(Flower_main.jpg) 0 0 0 0 stretch stretch; }")
        
        ##########
        self.lineEdit_Pass.setEchoMode(QtGui.QLineEdit.Password)  ##set to bullets      
        self.btn_Signup.clicked.connect(self.on_btn_Signup_clicked)

        self.btn_Login.clicked.connect(self.on_btn_Login_clicked)
        
            
    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login", None))
        self.label_pass.setText(_translate("LoginWindow", "Password", None))
        self.btn_Signup.setText(_translate("LoginWindow", "Sign up", None))
        self.btn_Login.setText(_translate("LoginWindow", "Login", None))
        self.label_user.setText(_translate("LoginWindow", "Username", None))
        self.label_3.setText(_translate("LoginWindow", "Flower Shop", None))


    def on_btn_Signup_clicked(self):
        self.NewUser = QtGui.QMainWindow()
        self.ui = create.Ui_NewUser(self.NewUser)
        self.ui.setupUi(self.NewUser)
        self.dialog=self.NewUser
        self.dialog.show()

        #login
    def on_btn_Login_clicked(self):
        user=self.lineEdit_User.text()
        password=self.lineEdit_Pass.text()
        obj=GetUserInfo(user,password)
        valid=obj.checkValid()
        if valid ==True:
         self.MainWindow = QtGui.QMainWindow()
         self.ui = main.Ui_MainWindow(user,password)
         self.ui.setupUi(self.MainWindow)
         self.dialog=self.MainWindow             
         self.dialog.show()

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    LoginWindow = QtGui.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

