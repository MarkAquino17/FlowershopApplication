# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainv3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sqlite3



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
    def loadData(self):# this part is the connecting of database to mainwindow
        connection = sqlite3.connect('ShopDatabase.db')
        
        query = "SELECT * FROM Stock"
        cursor=connection.cursor()
        result = connection.execute(query)
        
        
        self.tableWidget_2.setRowCount(0)
        
        
        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):   #change qtgui to qtapppl inpyqt5
                self.tableWidget_2.setItem(row_number, column_number, QtGui.QTableWidgetItem(str(data)))
                print(row_data)
                item=row_data
                print(item[0])


                #this code select a single row in the database table an doutputs it
        field1= connection.execute('SELECT * FROM Stock WHERE ItemName="Flower1"').fetchall()
        print(field1)
        connection.close()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(942, 748)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 3, 1, 1)
        self.btn_Load_5 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Load_5.sizePolicy().hasHeightForWidth())
        self.btn_Load_5.setSizePolicy(sizePolicy)
        self.btn_Load_5.setObjectName(_fromUtf8("btn_Load_5"))
        self.gridLayout.addWidget(self.btn_Load_5, 1, 4, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)
        self.btn_Load_3 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Load_3.sizePolicy().hasHeightForWidth())
        self.btn_Load_3.setSizePolicy(sizePolicy)
        self.btn_Load_3.setObjectName(_fromUtf8("btn_Load_3"))
        self.gridLayout.addWidget(self.btn_Load_3, 4, 0, 1, 2)
        self.btn_Load = QtGui.QPushButton(self.centralwidget)
        self.btn_Load.setObjectName(_fromUtf8("btn_Load"))
        self.gridLayout.addWidget(self.btn_Load, 4, 3, 1, 2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 2)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.tableWidget_3 = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy)
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(3)
        
        ## i think this removes the initial row in the table
##        self.tableWidget_3.setRowCount(6)
##        item = QtGui.QTableWidgetItem()
##        self.tableWidget_3.setVerticalHeaderItem(0, item)
##        item = QtGui.QTableWidgetItem()
##        self.tableWidget_3.setVerticalHeaderItem(1, item)
##        item = QtGui.QTableWidgetItem()
##        self.tableWidget_3.setVerticalHeaderItem(2, item)
##        item = QtGui.QTableWidgetItem()
##        self.tableWidget_3.setVerticalHeaderItem(3, item)
##        item = QtGui.QTableWidgetItem()
##        self.tableWidget_3.setVerticalHeaderItem(4, item)
##        item = QtGui.QTableWidgetItem()
##        self.tableWidget_3.setVerticalHeaderItem(5, item)
        
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, item)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(49)
        self.gridLayout.addWidget(self.tableWidget_3, 2, 0, 2, 2)
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.tableWidget_2 = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(6)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(49)
        self.gridLayout.addWidget(self.tableWidget_2, 2, 3, 2, 2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 3)
        self.btn_Load_4 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Load_4.sizePolicy().hasHeightForWidth())
        self.btn_Load_4.setSizePolicy(sizePolicy)
        self.btn_Load_4.setObjectName(_fromUtf8("btn_Load_4"))
        self.gridLayout.addWidget(self.btn_Load_4, 1, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.btn_Load_2 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Load_2.sizePolicy().hasHeightForWidth())
        self.btn_Load_2.setSizePolicy(sizePolicy)
        self.btn_Load_2.setObjectName(_fromUtf8("btn_Load_2"))
        self.gridLayout.addWidget(self.btn_Load_2, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 26))
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
        self.actionChange_User = QtGui.QAction(MainWindow)
        self.actionChange_User.setObjectName(_fromUtf8("actionChange_User"))
        self.menuUser.addAction(self.actionChange_User)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuUser.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #####
        header = self.tableWidget_2.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        header = self.tableWidget_3.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        
        self.btn_Load.clicked.connect(self.loadData)

        self.pushButton.clicked.connect(self.btn_lessthan_clicked)
        self.btn_Load_3.clicked.connect(self.btn_reset_clicked)
        self.pushButton_2.clicked.connect(self.btn_greaterthan_clicked)
        ###to do
        
    def btn_lessthan_clicked(self):
        
        
        self.rowPosition = self.tableWidget_3.rowCount() #gives rowPos the current rowcount
        print(self.rowPosition)
        self.selectedRow=self.tableWidget_2.currentRow() #gives selectedrow the currently clicked row's index
        col1=self.tableWidget_2.item(self.selectedRow,0) #selects the item at the current row, and column
        col2=self.tableWidget_2.item(self.selectedRow,1)
        col3=self.tableWidget_2.item(self.selectedRow,2)
        
        ###### to do quantity movement
        self.tableWidget_3.insertRow(self.rowPosition)  #insert a new row
        self.tableWidget_3.setItem(self.rowPosition , 0, QtGui.QTableWidgetItem(col1.text())) #insert item at the current row and col
        self.tableWidget_3.setItem(self.rowPosition , 1, QtGui.QTableWidgetItem(col2.text()))
        self.tableWidget_3.setItem(self.rowPosition , 2, QtGui.QTableWidgetItem(col3.text()))
        self.UpdatePrice()


    
    def btn_greaterthan_clicked(self):
        
        self.tableWidget_3.removeRow(self.tableWidget_3.currentRow())
        
        
    def btn_reset_clicked(self):
        self.tableWidget_3.setRowCount(0)
        
    def UpdatePrice(self):
        ctr=self.tableWidget_3.rowCount()
        price=0.00
        while ctr!=0:
            price=price+float(self.tableWidget_3.item(ctr-1,2).text())
            
            ctr=ctr-1
        
        self.label_3.setText("Total amount in cart:"+str(price))
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_Load_5.setText(_translate("MainWindow", "Search", None))
        self.pushButton.setText(_translate("MainWindow", "<", None))
        self.btn_Load_3.setText(_translate("MainWindow", "Reset", None))
        self.btn_Load.setText(_translate("MainWindow", "Load", None))
        self.label_2.setText(_translate("MainWindow", "Available in stock", None))
        self.pushButton_2.setText(_translate("MainWindow", ">", None))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantity", None))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price", None))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Cart", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Number available", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price per piece", None))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("MainWindow", "Total amount in cart:", None))
        self.btn_Load_4.setText(_translate("MainWindow", "Search", None))
        self.btn_Load_2.setText(_translate("MainWindow", "Purchase", None))
        self.menuUser.setTitle(_translate("MainWindow", "User", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help!!!!!????", None))##kek to edit
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionChange_User.setText(_translate("MainWindow", "Change User", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

