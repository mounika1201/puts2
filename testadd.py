import main
import unittest

class Test(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        def test_addint(self):
            rv =  self.app.get('/add?A=7&B=1')
            self.assertEqual(b'8.0', rv.result)
            self.assertNotEqual(b'6.000',rv.result)
        def test_addfloat(self):
            rv =  self.app.get('/add?A=6.7&B=2.2')
            self.assertEqual(b'8.9', rv.result)