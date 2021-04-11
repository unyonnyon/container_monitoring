import unittest

from prometheus_client import REGISTRY

from main import MyHandler


class TestMyHandler(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_counter_increment(self) -> None:
        before = REGISTRY.get_sample_value("get_request_count_total")
        MyHandler.update_metrics()
        after = REGISTRY.get_sample_value("get_request_count_total")
        self.assertEqual(1, after - before)
