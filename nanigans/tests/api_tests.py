import unittest

from mock import patch
from random import randint

from ..api import facebook, multichannel, publishers
from ..models import Response


class GetTimeRangesTests(unittest.TestCase):
    @patch('nanigans.models.Adapter.get')
    def test_get_timeranges_with_dummy_vars(self, mock_send):
        site = randint(100000, 999999)
        source = 'dummmySource'
        mock_send.return_value = Response()
        fb = facebook.get_timeranges()
        mc = multichannel.get_timeranges()
        pub = publishers.get_timeranges()
        self.assertIsInstance(fb, Response)
        self.assertIsInstance(mc, Response)
        self.assertIsInstance(pub, Response)

class GetAttributesTests(unittest.TestCase):
    @patch('nanigans.models.Adapter.get')
    def test_get_attribtues_with_dummy_vars(self, mock_send):
        site = randint(100000, 999999)
        source = 'dummmySource'
        mock_send.return_value = Response()
        fb = facebook.get_attributes()
        mc = multichannel.get_attributes()
        pub = publishers.get_attributes()
        self.assertIsInstance(fb, Response)
        self.assertIsInstance(mc, Response)
        self.assertIsInstance(pub, Response)

class GetMetricsTests(unittest.TestCase):
    @patch('nanigans.models.Adapter.get')
    def test_get_metrics_with_dummy_vars(self, mock_send):
        site = randint(100000, 999999)
        source = 'dummmySource'
        mock_send.return_value = Response()
        fb = facebook.get_metrics()
        mc = multichannel.get_metrics()
        pub = publishers.get_metrics()
        self.assertIsInstance(fb, Response)
        self.assertIsInstance(mc, Response)
        self.assertIsInstance(pub, Response)

class GetViewTests(unittest.TestCase):
    @patch('nanigans.models.Adapter.get')
    def test_get_view_with_dummy_vars(self, mock_send):
        site = randint(100000, 999999)
        source = 'dummmySource'
        view = randint(10000, 99999)
        mock_send.return_value = Response()
        fb = facebook.get_view(view)
        mc = multichannel.get_view(view)
        pub = publishers.get_view(view)
        self.assertIsInstance(fb, Response)
        self.assertIsInstance(mc, Response)
        self.assertIsInstance(pub, Response)

class GetStatsTests(unittest.TestCase):
    @patch('nanigans.models.Adapter.get')
    def test_get_stats_with_dummy_vars(self, mock_send):
        site = randint(100000, 999999)
        source = 'dummmySource'
        mock_send.return_value = Response()
        fb = facebook.get_stats()
        mc = multichannel.get_stats()
        pub = publishers.get_stats()
        self.assertIsInstance(fb, Response)
        self.assertIsInstance(mc, Response)
        self.assertIsInstance(pub, Response)


if __name__ == "__main__":
    test_cases = [
        GetTimeRangesTests,
        GetAttributesTests,
        GetMetricsTests,
        GetViewTests,
        GetStatsTests,
    ]

    for test_case in test_cases:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
        unittest.TextTestRunner(verbosity=1).run(suite)
