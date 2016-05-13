import unittest

from mock import patch
from random import randint

from ..api import get_attributes, get_metrics, get_timeranges, get_view, get_stats
from ..models import Response


class GetTimeRangesTests(unittest.TestCase):
    @patch('nanigans.models.Adapter.get')
    def test_get_timeranges_with_dummy_vars(self, mock_send):
        site = randint(100000, 999999)
        source = 'dummmySource'
        mock_send.return_value = Response()
        timeranges = get_timeranges(site,source)
        self.assertIsInstance(timeranges, Response)

class GetAttributesTests(unittest.TestCase):
    @patch('nanigans.models.Adapter.get')
    def test_get_attribtues_with_dummy_vars(self, mock_send):
        site = randint(100000, 999999)
        source = 'dummmySource'
        mock_send.return_value = Response()
        attributes = get_attributes(site,source)
        self.assertIsInstance(attributes, Response)

class GetMetricsTests(unittest.TestCase):
    @patch('nanigans.models.Adapter.get')
    def test_get_metrics_with_dummy_vars(self, mock_send):
        site = randint(100000, 999999)
        source = 'dummmySource'
        mock_send.return_value = Response()
        metrics = get_metrics(site,source)
        self.assertIsInstance(metrics, Response)

class GetViewTests(unittest.TestCase):
    @patch('nanigans.models.Adapter.get')
    def test_get_view_with_dummy_vars(self, mock_send):
        site = randint(100000, 999999)
        source = 'dummmySource'
        view = randint(10000, 99999)
        mock_send.return_value = Response()
        view = get_view(site,source,view)
        self.assertIsInstance(view, Response)

class GetStatsTests(unittest.TestCase):
    @patch('nanigans.models.Adapter.get')
    def test_get_stats_with_dummy_vars(self, mock_send):
        site = randint(100000, 999999)
        source = 'dummmySource'
        mock_send.return_value = Response()
        stats = get_stats(site,source)
        self.assertIsInstance(stats, Response)


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
        unittest.TextTestRunner(verbosity=5).run(suite)
