import football as football
import unittest

class TestDanger(unittest.TestCase):

    def test_danger(self):
        self.assertEqual(football.dangerous('1000000001'), 'YES')
        self.assertEqual(football.dangerous('1000000001'), 'YES')
        self.assertEqual(football.dangerous('1000000001'), 'YES')
        self.assertEqual(football.dangerous('1000000001'), 'YES')
        self.assertEqual(football.dangerous('1000000001'), 'YES')
        self.assertEqual(football.dangerous('1000000001'), 'YES')
        self.assertEqual(football.dangerous('1000001'), 'NO')

if __name__ == '__main__':
    unittest.main()