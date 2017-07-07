import unittest
from domain.infrastructure.location.stop_point import StopPoint
class TestStopPoint(unittest.TestCase):
    def test_constructor(self):
        stop_point = StopPoint(1, 2)
        self.assertEqual(stop_point.latitude, 2)
        self.assertEqual(stop_point.longtitude, 1)
