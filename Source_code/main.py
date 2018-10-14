# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainv3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sqlite3
import os
import sys
    #this part enables the relative path of the modules for importing
path=os.path.dirname(__file__)
fullpath=os.path.join(path,'BLL')
sys.path.append(fullpath)
sys.path.append('DAL')

from Get_User import GetUserInfo
from mainButtonControl import ButtonControl
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

class Ui_MainWindow(object):
    #the init function is used to send the user and password to this form
    def __init__(self, gUser="cheng",gPass="1234"):#TOOOOO EDDIIT 
        self.obj=GetUserInfo(gUser,gPass)
        self.user=self.obj.getUser()
        self.UserID=self.user[0][0]

    
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(915, 669)
        MainWindow.setEnabled(True) #to enable background in the GUI
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_stock = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_stock.setFont(font)
        self.label_stock.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stock.setObjectName(_fromUtf8("label_stock"))
        self.gridLayout.addWidget(self.label_stock, 0, 3, 1, 2)
        self.btn_Great = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Great.sizePolicy().hasHeightForWidth())
        self.btn_Great.setSizePolicy(sizePolicy)
        self.btn_Great.setObjectName(_fromUtf8("btn_Great"))
        self.gridLayout.addWidget(self.btn_Great, 4, 2, 1, 1)
        self.btn_Reset = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Reset.sizePolicy().hasHeightForWidth())
        self.btn_Reset.setSizePolicy(sizePolicy)
        self.btn_Reset.setObjectName(_fromUtf8("btn_Reset"))
        self.gridLayout.addWidget(self.btn_Reset, 5, 0, 1, 2)
        self.btn_Load = QtGui.QPushButton(self.centralwidget)
        self.btn_Load.setObjectName(_fromUtf8("btn_Load"))
        self.gridLayout.addWidget(self.btn_Load, 5, 3, 1, 2)
        self.tableWidget_Cart = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_Cart.sizePolicy().hasHeightForWidth())
        self.tableWidget_Cart.setSizePolicy(sizePolicy)
        self.tableWidget_Cart.setObjectName(_fromUtf8("tableWidget_Cart"))
        self.tableWidget_Cart.setColumnCount(3)
        self.tableWidget_Cart.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Cart.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Cart.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Cart.setHorizontalHeaderItem(2, item)
        self.tableWidget_Cart.horizontalHeader().setMinimumSectionSize(49)
        self.gridLayout.addWidget(self.tableWidget_Cart, 3, 0, 2, 2)
        self.label_Total = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Total.sizePolicy().hasHeightForWidth())
        self.label_Total.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_Total.setFont(font)
        self.label_Total.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Total.setObjectName(_fromUtf8("label_Total"))
        self.gridLayout.addWidget(self.label_Total, 6, 0, 1, 3)
        self.lineEdit_Search = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Search.setObjectName(_fromUtf8("lineEdit_Search"))
        self.gridLayout.addWidget(self.lineEdit_Search, 2, 3, 1, 1)
        self.btn_Search = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Search.sizePolicy().hasHeightForWidth())
        self.btn_Search.setSizePolicy(sizePolicy)
        self.btn_Search.setObjectName(_fromUtf8("btn_Search"))
        self.gridLayout.addWidget(self.btn_Search, 2, 4, 1, 1)
        self.btn_Less = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Less.sizePolicy().hasHeightForWidth())
        self.btn_Less.setSizePolicy(sizePolicy)
        self.btn_Less.setObjectName(_fromUtf8("btn_Less"))
        self.gridLayout.addWidget(self.btn_Less, 3, 2, 1, 1)
        self.btn_Purchase = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Purchase.sizePolicy().hasHeightForWidth())
        self.btn_Purchase.setSizePolicy(sizePolicy)
        self.btn_Purchase.setObjectName(_fromUtf8("btn_Purchase"))
        self.gridLayout.addWidget(self.btn_Purchase, 7, 1, 1, 1)
        self.tableWidget_Stock = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_Stock.sizePolicy().hasHeightForWidth())
        self.tableWidget_Stock.setSizePolicy(sizePolicy)
        self.tableWidget_Stock.setObjectName(_fromUtf8("tableWidget_Stock"))
        self.tableWidget_Stock.setColumnCount(3)
        self.tableWidget_Stock.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Stock.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Stock.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Stock.setHorizontalHeaderItem(2, item)
        self.tableWidget_Stock.horizontalHeader().setMinimumSectionSize(49)
        self.gridLayout.addWidget(self.tableWidget_Stock, 3, 3, 2, 2)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_cart = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cart.sizePolicy().hasHeightForWidth())
        self.label_cart.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_cart.setFont(font)
        self.label_cart.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cart.setObjectName(_fromUtf8("label_cart"))
        self.gridLayout.addWidget(self.label_cart, 0, 0, 1, 2)
        self.lineEdit_Search.raise_()
        self.btn_Search.raise_()
        self.btn_Great.raise_()
        self.btn_Reset.raise_()
        self.btn_Load.raise_()
        self.label_stock.raise_()
        self.tableWidget_Cart.raise_()
        self.label_cart.raise_()
        self.tableWidget_Stock.raise_()
        self.label_Total.raise_()
        self.btn_Purchase.raise_()
        self.label_4.raise_()
        self.btn_Less.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuUser = QtGui.QMenu(self.menubar)
        self.menuUser.setObjectName(_fromUtf8("menuUser"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionAccount_info = QtGui.QAction(MainWindow)
        self.actionAccount_info.setObjectName(_fromUtf8("actionAccount_info"))
        self.menuUser.addAction(self.actionAccount_info)

        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuUser.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #####
        MainWindow.setStyleSheet("#MainWindow { border-image: url(Flower_main2.jpg) 0 0 0 0 stretch stretch; }")
        self.tableWidget_Cart.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Stock.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        header = self.tableWidget_Stock.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        header = self.tableWidget_Cart.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        
        self.btn_Load.clicked.connect(self.btn_load_clicked)

        self.btn_Less.clicked.connect(self.btn_lessthan_clicked)
        self.btn_Reset.clicked.connect(self.btn_reset_clicked)
        self.btn_Great.clicked.connect(self.btn_greaterthan_clicked)
        
        self.btn_Purchase.clicked.connect(self.btn_purchase_clicked)
        
        self.actionAccount_info.triggered.connect(self.account_info_clicked)
        self.actionAbout.triggered.connect(self.About_clicked)
        
        self.actionHelp.triggered.connect(self.Help_clicked)
        self.btn_Search.clicked.connect(self.btn_search_clicked)
        
    def btn_load_clicked(self):# this part loads the database into the stock table
        result, connection, cursor=ButtonControl.loadData()
        
        self.tableWidget_Stock.setRowCount(0)    
        for row_number, row_data in enumerate(result): #iteration for inputting the database into the table
            self.tableWidget_Stock.insertRow(row_number)
            for column_number, data in enumerate(row_data):   
                self.tableWidget_Stock.setItem(row_number, column_number, QtGui.QTableWidgetItem(str(data)))
        cursor.close()    
        connection.close()       
    def btn_search_clicked(self):
        
        result, connection, cursor=ButtonControl.searchButton(self.lineEdit_Search.text())
        self.tableWidget_Stock.setRowCount(0)    
        for row_number, row_data in enumerate(result):
            self.tableWidget_Stock.insertRow(row_number)
            for column_number, data in enumerate(row_data):   
                self.tableWidget_Stock.setItem(row_number, column_number, QtGui.QTableWidgetItem(str(data)))
        cursor.close()
        connection.close()
        # the next three methods are for the menubar
    def Help_clicked(self):
        ButtonControl.helpButton()
        
    def About_clicked(self):
        ButtonControl.aboutButton()
        
    def account_info_clicked(self):
        self.obj.accountInfo()

        
    def btn_lessthan_clicked(self):
        
        
        self.rowPosition = self.tableWidget_Cart.rowCount() #gives rowPos the current rowcount
       
        self.selectedRow=self.tableWidget_Stock.currentRow() #gives selectedrow the currently clicked row's index
        col1=self.tableWidget_Stock.item(self.selectedRow,0) #selects the item at the current row, and column
        col2=self.tableWidget_Stock.item(self.selectedRow,1)
        col3=self.tableWidget_Stock.item(self.selectedRow,2)
        
        #update the price and quantity if the item is already in the cart
        dup=False
        rowCtr=0
        while rowCtr!=self.tableWidget_Cart.rowCount():
            if self.tableWidget_Cart.item(rowCtr,0).text()==self.tableWidget_Stock.item(self.selectedRow,0).text():
                dup=True
                quantity=int(self.tableWidget_Cart.item(rowCtr,1).text())
                if quantity ==int(self.tableWidget_Stock.item(self.selectedRow,1).text()):
                 ButtonControl.lessThanError(0) #error when the user is getting more item than available
                else: 
                 self.tableWidget_Cart.setItem(rowCtr , 1, QtGui.QTableWidgetItem(str(quantity+1)))
                 self.itemPrice=float(col3.text())
                 newPrice=self.itemPrice*(quantity+1)
                 self.tableWidget_Cart.setItem(rowCtr , 2, QtGui.QTableWidgetItem(str(newPrice)))
                
                break
            rowCtr+=1
        
        #insert a new row if the item is not yet in the cart
        if dup==False:
            if int(self.tableWidget_Stock.item(self.selectedRow,1).text())==0:
                ButtonControl.lessThanError(1)
            else:
             self.tableWidget_Cart.insertRow(self.rowPosition)  #insert a new row
             self.tableWidget_Cart.setItem(self.rowPosition , 0, QtGui.QTableWidgetItem(col1.text())) #insert item at the current row and col
             self.tableWidget_Cart.setItem(self.rowPosition , 1, QtGui.QTableWidgetItem("1"))
             self.tableWidget_Cart.setItem(self.rowPosition , 2, QtGui.QTableWidgetItem(col3.text()))
        
        self.UpdatePrice()


    
    def btn_greaterthan_clicked(self): #return item from the cart to the stock table
        if self.tableWidget_Cart.item(self.tableWidget_Cart.currentRow(),1)==None:
            return
        else:
         if int(self.tableWidget_Cart.item(self.tableWidget_Cart.currentRow(),1).text())>1:
            quantity=int(self.tableWidget_Cart.item(self.tableWidget_Cart.currentRow(),1).text())-1
            self.tableWidget_Cart.setItem(self.tableWidget_Cart.currentRow() , 1, QtGui.QTableWidgetItem(str(quantity)))
            
            
            newPrice=(float(self.tableWidget_Cart.item(self.tableWidget_Cart.currentRow(),2).text()))/(quantity+1)
            newPrice=newPrice*quantity
            self.tableWidget_Cart.setItem(self.tableWidget_Cart.currentRow() , 2, QtGui.QTableWidgetItem(str(newPrice)))
         else:    
            self.tableWidget_Cart.removeRow(self.tableWidget_Cart.currentRow())
        self.UpdatePrice()
        
    def btn_reset_clicked(self): #empty the cart table
        self.tableWidget_Cart.setRowCount(0)
        self.label_Total.setText("Total amount in cart:0.0")
    def btn_purchase_clicked(self): #this updates the database, reloads the stock table, and resets the cart table.
        if self.tableWidget_Cart.rowCount()==0:
          ButtonControl.checkCart(True,0,0,0)

        else:   
          rowCount=0
          itemID=""
          
          
          while rowCount<self.tableWidget_Cart.rowCount():
              
              itemID=itemID+ButtonControl.itemID(self.tableWidget_Cart.item(rowCount,0).text(),self.tableWidget_Cart.item(rowCount,1).text())
              rowCount=rowCount+1
          calcel=False
          cancel=ButtonControl.checkCart(False,self.price,self.UserID,itemID)
          if cancel==False:
           self.btn_load_clicked()
           self.btn_reset_clicked()
    def UpdatePrice(self): #update the price in the GUI.
        ctr=self.tableWidget_Cart.rowCount()
        self.price=0.00
        while ctr!=0:
            self.price=self.price+float(self.tableWidget_Cart.item(ctr-1,2).text())
            
            ctr=ctr-1
        
        self.label_Total.setText("Total amount in cart:"+str(self.price))
     
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Flower Shop", None))
        self.label_stock.setText(_translate("MainWindow", "Available in stock", None))
        self.btn_Great.setText(_translate("MainWindow", ">", None))
        self.btn_Reset.setText(_translate("MainWindow", "Reset", None))
        self.btn_Load.setText(_translate("MainWindow", "Load", None))
        item = self.tableWidget_Cart.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_Cart.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantity", None))
        item = self.tableWidget_Cart.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price", None))
        self.label_Total.setText(_translate("MainWindow", "Total amount in cart: P 0.00", None))
        self.btn_Search.setText(_translate("MainWindow", "Search", None))
        self.btn_Less.setText(_translate("MainWindow", "<", None))
        self.btn_Purchase.setText(_translate("MainWindow", "Purchase", None))
        item = self.tableWidget_Stock.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_Stock.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Number available", None))
        item = self.tableWidget_Stock.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price per piece", None))
        self.label_4.setText(_translate("MainWindow", " ", None))
        self.label_cart.setText(_translate("MainWindow", "Cart", None))
        self.menuUser.setTitle(_translate("MainWindow", "User", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionAccount_info.setText(_translate("MainWindow", "Account info", None))



if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

