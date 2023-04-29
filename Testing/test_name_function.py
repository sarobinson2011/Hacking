import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ Tests for 'name_function.py' """
    def test_first_last_name(self):
        """ Do names like 'Donald Trump' work? """
        formatted_name = get_formatted_name('donald', '', 'trump')
        self.assertEqual(formatted_name, 'Donald Trump')

    def test_first_middle_last_name(self):
        """ Do names like Stephen Andrew Robinson work? """
        formatted_name = get_formatted_name('stephen', 'andrew', 'robinson')
        self.assertEqual(formatted_name, 'Stephen Andrew Robinson')

if __name__ == '__main__':
    unittest.main()

