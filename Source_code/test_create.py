import unittest
from create import Ui_NewUser

class test_create(unittest.TestCase):

    def test_on_pushButton_clicked_create(self):
        self.assertTrue(Ui_NewUser().on_pushButton_clicked_create,True)

if __name__=='__main__':
    unittest.main()
