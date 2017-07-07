import unittest
from domain.infrastructure.location.stop_location import StopLocation
from domain.infrastructure.location.stop_location_type import StopLocationType


class TestStopLocation(unittest.TestCase):
    def test_constructor(self):
        stop_location = StopLocation(1, 2, "Орлов Мост")
        self.assertEqual(stop_location.latitude, 2)
        self.assertEqual(stop_location.longtitude, 1)
        self.assertEqual(stop_location.name, "Орлов Мост")
