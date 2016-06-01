import unittest

from datetime import datetime
from ..utils import generate_date_chunks, generate_dates


class GenerateDateRangeTests(unittest.TestCase):
    def test_generate_dates_works(self):
        start = '2016-05-25'
        stop = '2016-06-05'
        output = generate_dates(start, stop)
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

    def test_generate_dates_on_single_day(self):
        start = '2016-06-05'
        stop = '2016-06-06'
        output = generate_dates(start, stop)
        desired_end_date_output = '2016-06-05'
        desired_list_output = ['2016-06-05']
        self.assertEqual(output, desired_list_output)
        self.assertEqual(desired_list_output.pop(), start)
        self.assertEqual(desired_end_date_output, output[0])


class GenerateDateChunksTest(unittest.TestCase):

    start = '2016-01-01'
    end = '2016-06-01'
    length1 = 1
    length2 = 10
    length3 = 25
    length4 = 31

    def test_generate_date_chunks_1(self):
        generator = generate_date_chunks(self.start, self.end, self.length1)
        output = [dates for dates in generator]
        diff = datetime.strptime(self.end, '%Y-%m-%d')-datetime.strptime(self.start, '%Y-%m-%d')
        check = divmod(diff.days, self.length1)
        if check[1] == 0:
            self.assertEqual(check[0],len(output))
        else:
            self.assertEqual(check[0]+1, len(output))

    def test_generate_date_chunks_10(self):
        generator = generate_date_chunks(self.start, self.end, self.length2)
        output = [dates for dates in generator]
        diff = datetime.strptime(self.end, '%Y-%m-%d')-datetime.strptime(self.start, '%Y-%m-%d')
        check = divmod(diff.days, self.length2)
        if check[1] == 0:
            self.assertEqual(check[0],len(output))
        else:
            self.assertEqual(check[0]+1, len(output))

    def test_generate_date_chunks_25(self):
        generator = generate_date_chunks(self.start, self.end, self.length3)
        output = [dates for dates in generator]
        diff = datetime.strptime(self.end, '%Y-%m-%d')-datetime.strptime(self.start, '%Y-%m-%d')
        check = divmod(diff.days, self.length3)
        if check[1] == 0:
            self.assertEqual(check[0],len(output))
        else:
            self.assertEqual(check[0]+1, len(output))

    def test_generate_date_chunks_31(self):
        generator = generate_date_chunks(self.start, self.end, self.length4)
        output = [dates for dates in generator]
        diff = datetime.strptime(self.end, '%Y-%m-%d')-datetime.strptime(self.start, '%Y-%m-%d')
        check = divmod(diff.days, self.length4)
        if check[1] == 0:
            self.assertEqual(check[0],len(output))
        else:
            self.assertEqual(check[0]+1, len(output))
           

if __name__ == "__main__":
    test_cases = [GenerateDateRangeTests, GenerateDateChunksTest]

    for test_case in test_cases:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
        unittest.TextTestRunner(verbosity=5).run(suite)


