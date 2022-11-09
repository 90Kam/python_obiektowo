import unittest

from dane import dana1,dana2,dana3,dana4

class Pierwszy_unittest(unittest.TestCase):
    def test_dodawania(self): 
        self.assertEqual((dana4+dana2), dana4)
    def test_prawdy(self):
        self.assertTrue(dana3,dana1)
if __name__ == '__main__':
        unittest.main()
        

    