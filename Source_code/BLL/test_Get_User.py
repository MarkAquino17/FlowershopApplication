import unittest

from Get_User import GetUserInfo

class test_Get_User(unittest.TestCase):
    
    def test_checkInfo(self):
        self.assertTrue(GetUserInfo('cheng',1234).checkInfo,True)
            
        
    def test_getUser(self):
        self.assertTrue(GetUserInfo('cheng',1234).getUser,True)

    def test_accountInfo(self):
        self.assertTrue(GetUserInfo('cheng',1234).accountInfo,True)
        

if __name__=='__main__':
    unittest.main()
