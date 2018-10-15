import unittest
from mainButtonControl import ButtonControl

class test_mainButtonControl(unittest.TestCase):
    def test_loadData(self):
        self.assertTrue(ButtonControl().loadData,True)
    def test_searchButton(self):
        self.assertTrue(ButtonControl().searchButton,True)
        
if __name__=='__main__':
    unittest.main()
