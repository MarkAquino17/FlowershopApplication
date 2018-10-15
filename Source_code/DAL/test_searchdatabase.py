import unittest
from searchdatabase import Search

class test_searchdatabase(unittest.TestCase):
    def test_CheckInfo(self):
        self.assertTrue(Search().CheckInfo,True)
    def test_getInfo(self):
        self.assertTrue(Search().getInfo,True)
    def test_loadDatabase(self):
        self.assertTrue(Search().loadDatabase,True)
    def test_searchDatabase(self):
        self.assertTrue(Search().searchDatabase,True)    
    
if __name__=='__main__':
    unittest.main()
