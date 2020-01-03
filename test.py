import main
import unittest

class Test(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

       
