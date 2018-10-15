import unittest
from login import Ui_LoginWindow

class test_login(unittest.TestCase):
    def test_on_btn_Signup_clicked(self):
        self.assertTrue(Ui_LoginWindow().on_btn_Signup_clicked,True)

    def test_on_btn_Login_clicked(self):
        self.assertTrue(Ui_LoginWindow().on_btn_Login_clicked,True)

if __name__=='__main__':
    unittest.main()
