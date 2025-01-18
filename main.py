import unittest

from shapes import Palpite

class TestShots(unittest.TestCase):

    def test_palpite_maior(self):
        palpite = Palpite(1, 3)
        self.assertEqual(palpite.shot(), 1)

    def test_palpite_igual(self):
        palpite = Palpite(3, 3)
        self.assertEqual(palpite.shot(), 0)

    def test_palpite_menor(self):
        palpite = Palpite(3, 1)
        self.assertEqual(palpite.shot(), -1)


if __name__ == '__main__':
    unittest.main()
