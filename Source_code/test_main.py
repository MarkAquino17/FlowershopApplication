import unittest
from main import Ui_MainWindow

class test_main(unittest.TestCase):

    def test_btn_load_clicked(self):
        self.assertTrue(Ui_MainWindow().btn_load_clicked,True)
        
    def test_btn_search_clicked(self):
        self.assertTrue(Ui_MainWindow().btn_search_clicked,True)
        
    def test_Help_clicked(self):
        self.assertTrue(Ui_MainWindow().btn_load_clicked,True)
        
    def test_Help_clicked(self):
        self.assertTrue(Ui_MainWindow().Help_clicked,True)
        
    def test_About_clicked(self):
        self.assertTrue(Ui_MainWindow().About_clicked,True)
        
    def test_btn_lessthan_clicked(self):
        self.assertTrue(Ui_MainWindow().btn_lessthan_clicked,True)
        
    def test_btn_greaterthan_clicked(self):
        self.assertTrue(Ui_MainWindow().btn_greaterthan_clicked,True)

    def test_btn_reset_clicked(self):
        self.assertTrue(Ui_MainWindow().btn_reset_clicked,True)
        
    def test_btn_purchase_clicked(self):
        self.assertTrue(Ui_MainWindow().btn_purchase_clicked,True)
        
    def test_UpdatePrice(self):
        self.assertTrue(Ui_MainWindow().UpdatePrice,True)
        

        

if __name__=='__main__':
    unittest.main()
