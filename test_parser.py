import unittest
from test_parser import parse_hh

class TestParser(unittest.TestCase):
    def test_parse_hh(self):
        vacancies = parse_hh('Python developer')
        self.assertTrue(len(vacancies) > 0)

if __name__ == '__main__':
    unittest.main()