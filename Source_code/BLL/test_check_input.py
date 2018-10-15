import unittest
from check_input import CheckCreateInput

class test_check_input(unittest.TestCase):

    def test_SaveUser(self):
        self.assertTrue(CheckCreateInput().SaveUser,True)

if __name__=='__main__':
    unittest.main()
