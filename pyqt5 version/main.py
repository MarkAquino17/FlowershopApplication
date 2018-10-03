# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainv3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

import sqlite3

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    #the init function is used to send the user and password to this form
    def __init__(self, gUser="cyrill",gPass="12346"):#TOOOOO EDDIIT
        self.gUser=gUser
        self.gPass=gPass
        connection = sqlite3.connect('ShopDatabase.db')
        cursor=connection.cursor()
        getUser=connection.execute('SELECT UserID,Name,ContactNo,Address FROM Users WHERE Username=? AND Password=?',[self.gUser,self.gPass]).fetchall()
        self.UserID=getUser[0][0]
        self.Name=getUser[0][1]
        self.Contact=getUser[0][2]
        self.Address=getUser[0][3]

        cursor.close()
        connection.close()
    def loadData(self):# this part is the connecting of database to mainwindow
        connection = sqlite3.connect('ShopDatabase.db')
        
        query = "SELECT ItemName,Quantity,ItemPrice FROM Stock"
        cursor=connection.cursor()
        result = connection.execute(query)
        self.tableWidget_Stock.setRowCount(0)    
        for row_number, row_data in enumerate(result):
            self.tableWidget_Stock.insertRow(row_number)
            for column_number, data in enumerate(row_data):   
                self.tableWidget_Stock.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        cursor.close()
        connection.close()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 669)
        MainWindow.setEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_stock = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_stock.setFont(font)
        self.label_stock.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stock.setObjectName("label_stock")
        self.gridLayout.addWidget(self.label_stock, 0, 3, 1, 2)
        self.btn_Great = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Great.sizePolicy().hasHeightForWidth())
        self.btn_Great.setSizePolicy(sizePolicy)
        self.btn_Great.setObjectName("btn_Great")
        self.gridLayout.addWidget(self.btn_Great, 4, 2, 1, 1)
        self.btn_Reset = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Reset.sizePolicy().hasHeightForWidth())
        self.btn_Reset.setSizePolicy(sizePolicy)
        self.btn_Reset.setObjectName("btn_Reset")
        self.gridLayout.addWidget(self.btn_Reset, 5, 0, 1, 2)
        self.btn_Load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Load.setObjectName("btn_Load")
        self.gridLayout.addWidget(self.btn_Load, 5, 3, 1, 2)
        self.tableWidget_Cart = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_Cart.sizePolicy().hasHeightForWidth())
        self.tableWidget_Cart.setSizePolicy(sizePolicy)
        self.tableWidget_Cart.setObjectName("tableWidget_Cart")
        self.tableWidget_Cart.setColumnCount(3)
        self.tableWidget_Cart.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Cart.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Cart.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Cart.setHorizontalHeaderItem(2, item)
        self.tableWidget_Cart.horizontalHeader().setMinimumSectionSize(49)
        self.gridLayout.addWidget(self.tableWidget_Cart, 3, 0, 2, 2)
        self.label_Total = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Total.sizePolicy().hasHeightForWidth())
        self.label_Total.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_Total.setFont(font)
        self.label_Total.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Total.setObjectName("label_Total")
        self.gridLayout.addWidget(self.label_Total, 6, 0, 1, 3)
        self.lineEdit_Search = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Search.setObjectName("lineEdit_Search")
        self.gridLayout.addWidget(self.lineEdit_Search, 2, 3, 1, 1)
        self.btn_Search = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Search.sizePolicy().hasHeightForWidth())
        self.btn_Search.setSizePolicy(sizePolicy)
        self.btn_Search.setObjectName("btn_Search")
        self.gridLayout.addWidget(self.btn_Search, 2, 4, 1, 1)
        self.btn_Less = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Less.sizePolicy().hasHeightForWidth())
        self.btn_Less.setSizePolicy(sizePolicy)
        self.btn_Less.setObjectName("btn_Less")
        self.gridLayout.addWidget(self.btn_Less, 3, 2, 1, 1)
        self.btn_Purchase = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Purchase.sizePolicy().hasHeightForWidth())
        self.btn_Purchase.setSizePolicy(sizePolicy)
        self.btn_Purchase.setObjectName("btn_Purchase")
        self.gridLayout.addWidget(self.btn_Purchase, 7, 1, 1, 1)
        self.tableWidget_Stock = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_Stock.sizePolicy().hasHeightForWidth())
        self.tableWidget_Stock.setSizePolicy(sizePolicy)
        self.tableWidget_Stock.setObjectName("tableWidget_Stock")
        self.tableWidget_Stock.setColumnCount(3)
        self.tableWidget_Stock.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Stock.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Stock.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Stock.setHorizontalHeaderItem(2, item)
        self.tableWidget_Stock.horizontalHeader().setMinimumSectionSize(49)
        self.gridLayout.addWidget(self.tableWidget_Stock, 3, 3, 2, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_cart = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cart.sizePolicy().hasHeightForWidth())
        self.label_cart.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_cart.setFont(font)
        self.label_cart.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cart.setObjectName("label_cart")
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
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 26))
        self.menubar.setObjectName("menubar")
        self.menuUser = QtWidgets.QMenu(self.menubar)
        self.menuUser.setObjectName("menuUser")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAccount_info = QtWidgets.QAction(MainWindow)
        self.actionAccount_info.setObjectName("actionAccount_info")
        self.menuUser.addAction(self.actionAccount_info)

        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuUser.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #####
        MainWindow.setStyleSheet("#MainWindow { border-image: url(Flower_main2.jpg) 0 0 0 0 stretch stretch; }")
        self.tableWidget_Cart.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Stock.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        header = self.tableWidget_Stock.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header = self.tableWidget_Cart.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        
        self.btn_Load.clicked.connect(self.loadData)

        self.btn_Less.clicked.connect(self.btn_lessthan_clicked)
        self.btn_Reset.clicked.connect(self.btn_reset_clicked)
        self.btn_Great.clicked.connect(self.btn_greaterthan_clicked)
        
        self.btn_Purchase.clicked.connect(self.btn_purchase_clicked)
        
        self.actionAccount_info.triggered.connect(self.account_info_clicked)
        self.actionAbout.triggered.connect(self.About_clicked)
        
        self.actionHelp.triggered.connect(self.Help_clicked)
        self.btn_Search.clicked.connect(self.btn_search_clicked)

    def btn_search_clicked(self):
        search=self.lineEdit_Search.text()
        connection = sqlite3.connect('ShopDatabase.db')
        c=connection.cursor()
        print(search)
        result=c.execute("SELECT ItemName,Quantity,ItemPrice FROM Stock WHERE ItemName LIKE ?",('%'+search+'%',))
        self.tableWidget_Stock.setRowCount(0)    
        for row_number, row_data in enumerate(result):
            self.tableWidget_Stock.insertRow(row_number)
            for column_number, data in enumerate(row_data):   
                self.tableWidget_Stock.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.commit()
        c.close()
        connection.close()

        # the next three methods are for the menubar
    def Help_clicked(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("    ")
        msg.setInformativeText( "      ") 
        msg.setWindowTitle("Help")
        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        
	
        retval = msg.exec_()
    def About_clicked(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("Name")
        msg.setInformativeText("Info ") 
        msg.setWindowTitle("About")
        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        
	
        retval = msg.exec_()
        
    def account_info_clicked(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("Name: "+self.Name)
        msg.setInformativeText("Username: "+self.gUser+"\n User ID: "+str(self.UserID)+"\n Contact: "+str(self.Contact)+"\n Address: "+self.Address)
        msg.setWindowTitle("Account Details")
        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        
	
        retval = msg.exec_()

        
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
                self.tableWidget_Cart.setItem(rowCtr , 1, QtWidgets.QTableWidgetItem(str(quantity+1)))
                self.itemPrice=float(col3.text())
                newPrice=self.itemPrice*(quantity+1)
                self.tableWidget_Cart.setItem(rowCtr , 2, QtWidgets.QTableWidgetItem(str(newPrice)))
                
                break
            rowCtr+=1
        
        #insert a new row if the item is not yet in the cart
        if dup==False:
            
            self.tableWidget_Cart.insertRow(self.rowPosition)  #insert a new row
            self.tableWidget_Cart.setItem(self.rowPosition , 0, QtWidgets.QTableWidgetItem(col1.text())) #insert item at the current row and col
            self.tableWidget_Cart.setItem(self.rowPosition , 1, QtWidgets.QTableWidgetItem("1"))
            self.tableWidget_Cart.setItem(self.rowPosition , 2, QtWidgets.QTableWidgetItem(col3.text()))
        
        self.UpdatePrice()


    
    def btn_greaterthan_clicked(self):
        if self.tableWidget_Cart.item(self.tableWidget_Cart.currentRow(),1)==None:
            return
        else:
         if int(self.tableWidget_Cart.item(self.tableWidget_Cart.currentRow(),1).text())>1:
            quantity=int(self.tableWidget_Cart.item(self.tableWidget_Cart.currentRow(),1).text())-1
            self.tableWidget_Cart.setItem(self.tableWidget_Cart.currentRow() , 1, QtWidgets.QTableWidgetItem(str(quantity)))
            
            
            newPrice=(float(self.tableWidget_Cart.item(self.tableWidget_Cart.currentRow(),2).text()))/(quantity+1)
            newPrice=newPrice*quantity
            self.tableWidget_Cart.setItem(self.tableWidget_Cart.currentRow() , 2, QtWidgets.QTableWidgetItem(str(newPrice)))
         else:    
            self.tableWidget_Cart.removeRow(self.tableWidget_Cart.currentRow())
        self.UpdatePrice()
        
    def btn_reset_clicked(self):
        self.tableWidget_Cart.setRowCount(0)
        self.label_Total.setText("Total amount in cart:0.0")
    def btn_purchase_clicked(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("Are you done purchasing?")
        
        msg.setWindowTitle("Confirmation")
        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        
	
        retval = msg.exec_()
        
        print ("value of pressed message box button:", retval)
        if retval==1024:
         connection = sqlite3.connect('ShopDatabase.db')
         c=connection.cursor()
         now = datetime.datetime.now()
         time=now.strftime("%Y-%m-%d %H:%M")
         c.execute("INSERT INTO Purchase (UserID,OrderDate,Bill) VALUES (?,?,?)",(self.UserID,time,self.price))
         connection.commit()
         c.close()
         connection.close()
    def UpdatePrice(self):
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
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
