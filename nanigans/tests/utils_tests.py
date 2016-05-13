import unittest

from datetime import datetime, timedelta
from ..utils import generate_date_range


class GenerateDateRangeTests(unittest.TestCase):
    def test_generate_date_range_works(self):
        start = '2016-05-25'
        stop = '2016-06-05'
        output = generate_date_range(start, stop)
        desired_end_date_output = '2016-06-04'
        desired_list_output = [
            '2016-06-04', 
            '2016-06-03', 
            '2016-06-02', 
            '2016-06-01', 
            '2016-05-31', 
            '2016-05-30', 
            '2016-05-29', 
            '2016-05-28', 
            '2016-05-27', 
            '2016-05-26', 
            '2016-05-25'
        ]
        self.assertEqual(output, desired_list_output)
        self.assertEqual(desired_list_output.pop(), start)
        self.assertEqual(desired_end_date_output, output[0])

    def test_generate_date_range_on_single_day(self):
        start = '2016-06-05'
        stop = '2016-06-06'
        output = generate_date_range(start, stop)
        desired_end_date_output = '2016-06-05'
        desired_list_output = ['2016-06-05']
        self.assertEqual(output, desired_list_output)
        self.assertEqual(desired_list_output.pop(), start)
        self.assertEqual(desired_end_date_output, output[0])


if __name__ == "__main__":
    test_cases = [GenerateDateRangeTests]

    for test_case in test_cases:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
        unittest.TextTestRunner(verbosity=5).run(suite)


