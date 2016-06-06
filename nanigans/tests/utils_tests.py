import unittest
import re

from random import randint
from datetime import datetime
from ..config import NAN_CONFIG as config 
from ..utils import generate_date_chunks, generate_dates, generate_token, reassign


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

class GenerateTokenTests(unittest.TestCase):
    test_user_1 = 'test@gmail.com'
    test_user_2 = 'fake2@fake.com'
    test_password_1 = 'test'
    test_password_2 = 'fakepass2'
    test_site_1 = '456789'
    test_site_2 = '123456'

    def test_generate_token_returns_token(self):
        token1 = generate_token(self.test_user_1, self.test_password_1, self.test_site_1)
        token2 = generate_token(self.test_user_2, self.test_password_2, self.test_site_2)
        self.assertIsInstance(token1, str)
        self.assertIsNone(token2)

    def test_generate_token_returns_token_in_proper_format(self):
        b64regex = '\w{8}-\w{4}-\w{4}-\w{4}-\w{12}'
        expr = re.compile(b64regex)
        token1 = generate_token(self.test_user_1, self.test_password_1, self.test_site_1)
        token2 = 'this123!-sho7778uld-no8459t-match888'
        self.assertIsNotNone(expr.match(token1))
        self.assertIsNone(expr.match(token2))

class ReassignTests(unittest.TestCase):
    site = randint(10000, 99999)
    
    def test_reassign_changes_site(self):
        before = config['site']
        reassign(self.site)
        after = config['site']
        self.assertFalse(before==after)

    def test_reassign_changes_token(self):
        before = config['token']
        reassign(self.site)
        after = config['token']
        self.assertFalse(before==after)

if __name__ == "__main__":
    test_cases = [GenerateDateRangeTests, GenerateDateChunksTest, GenerateTokenTests, ReassignTests]
    for test_case in test_cases:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
        unittest.TextTestRunner(verbosity=5).run(suite)


