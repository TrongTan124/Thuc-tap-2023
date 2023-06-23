import unittest
import bubblesort as st
import file_max_cell as fc

class Project_Test(unittest.TestCase):
    def test_bsort(self):
        test_list = [4,3,2,1]
        expected = [1,2,3,4]
        actual = st.bubblesort(test_list)
        self.assertEqual(expected, actual)

    def test_des(self):
        test_list = [1,2,5,4,3]
        expected = [5,4,3,2,1]
        actual = st.bubblesort(test_list)
        self.assertEqual(expected, actual)
    
    def test_empty(self):
        test_list = []
        expected = []
        actual = st.bubblesort(test_list)
        self.assertEqual(expected, actual)

    def test_file_max_cell(self):
        a_max, a_series = fc.file_max_cell('scores.csv', 'math_score')
        self.assertEqual(a_max, 100)
        self.assertEqual(len(a_series), 8)