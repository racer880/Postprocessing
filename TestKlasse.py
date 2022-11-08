import unittest as ut

class TestKlasse(ut.TestCase):
    def test_gerade(self):
        self.assertEqual(2%2, 0)

if(__name__) == '__main__':
    ut.main()