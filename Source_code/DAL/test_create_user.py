import unittest
from create_user import CreateUser

class test_create__user(unittest.TestCase):
    
    def test_CheckUsername(self):
        self.assertTrue(CreateUser().CheckUsername,True)
    
    def test_InsertNewUser(self):
        self.assertTrue(CreateUser().InsertNewUser,True)

if __name__=='__main__':
    unittest.main()
