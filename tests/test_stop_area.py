import unittest
from domain.infrastructure.location.stop_area import StopArea
from domain.infrastructure.location.stop_area import StopLocation
class TestStopArea(unittest.TestCase):
    def test_constructor(self):
        stop_area = StopArea(latitude = 2, longtitude = 1, stop_locations = [StopLocation(1,2)])
        self.assertEqual(stop_area.latitude, 2)
        self.assertEqual(stop_area.longtitude, 1)
        self.assertEqual(len(stop_area.stop_locations), 1)