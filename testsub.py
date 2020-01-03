import main
import unittest

class Test(unittest.TestCase):

        def setUp(self):
            main.app.testing = True

 self.app = main.app.test_client()
			 def test_subint(self):
            rv =  self.app.get('/sub?A=5&B=3')
            self.assertEqual(b'2.0', rv.result)
            self.assertNotEqual(b'6.000',rv.result)
        def test_subfloat(self):
            rv =  self.app.get('/sub?A=4.1&B=2.2')
            self.assertEqual(b'3.0', rv.result)