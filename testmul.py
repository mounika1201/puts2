import main
import unittest

class Test(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()
			
  def test_mulint(self):
            rv =  self.app.get('/mul?A=5&B=5')
            self.assertEqual(b'25', rv.result)
            self.assertNotEqual(b'6.000',rv.result)
        def test_mulfloat(self):
            rv =  self.app.get('/mul?A=2.0&B=3.4')
            self.assertEqual(b'6.8', rv.result)