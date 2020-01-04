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
            self.app = main.app.test_client()
        def test_subint(self):
            rv =  self.app.get('/sub?A=5&B=3')
            self.assertEqual(b'2.0', rv.result)
            self.assertNotEqual(b'6.000',rv.result)
        def test_subfloat(self):
            rv =  self.app.get('/sub?A=4.1&B=2.2')
            self.assertEqual(b'3.0', rv.result)
        def test_mulint(self):
            rv =  self.app.get('/mul?A=5&B=5')
            self.assertEqual(b'25', rv.result)
            self.assertNotEqual(b'6.000',rv.result)
        def test_mulfloat(self):
            rv =  self.app.get('/mul?A=2.0&B=3.4')
            self.assertEqual(b'6.8', rv.result)
        def test_divint(self):
            rv =  self.app.get('/div?A=10&B=5')
            self.assertEqual(b'2', rv.result)
            self.assertNotEqual(b'0.0256',rv.r̥esult)
        def test_divfloat(self):
            rv =  self.app.get('/div?A=5.3&B=6.2')
            self.assertEqual(b'0.854', rv.result)
       
