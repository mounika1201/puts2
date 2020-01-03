import main
import unittest

class Test(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()
def test_divint(self):
            rv =  self.app.get('/div?A=10&B=5')
            self.assertEqual(b'2', rv.result)
            self.assertNotEqual(b'0.0256',rv.r̥esult)
        def test_divfloat(self):
            rv =  self.app.get('/div?A=5.3&B=6.2')
            self.assertEqual(b'0.854', rv.result)