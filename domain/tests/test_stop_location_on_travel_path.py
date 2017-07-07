import unittest

from datetime import datetime, timedelta

from domain.infrastructure.location.stop_location_on_travel_path import StopLocationOnTravelPath
from domain.infrastructure.location.stop_location_type import StopLocationType


class TestStopLocation(unittest.TestCase):
    def test_constructor(self):
        stop_location = StopLocationOnTravelPath(1, 2, arrival_time=datetime.now(),
                                                 departure_time=datetime.now() + timedelta(minutes=2))
        self.assertEqual(stop_location.type, StopLocationType.STOP)
        stop_location = StopLocationOnTravelPath(1, 2, location_type=StopLocationType.TRANSFER,
                                                 arrival_time=datetime.now(),
                                                 departure_time=datetime.now() + timedelta(minutes=2))
        self.assertEqual(stop_location.type, StopLocationType.TRANSFER)

    def test_date_assignment(self):
        with self.assertRaises(ValueError) as context:
            stop_location = StopLocationOnTravelPath(1, 2, arrival_time=datetime.now() + timedelta(minutes=2),
                                                     departure_time=datetime.now())
        self.assertEqual(str(context.exception), "150000")

    def test_equality_comparison(self):
        stop_location = StopLocationOnTravelPath(1, 2, arrival_time=datetime.now(),
                                                 departure_time=datetime.now() + timedelta(minutes=2))
        equal_stop_location = StopLocationOnTravelPath(1, 2, arrival_time=stop_location.arrival_time,
                                                       departure_time=stop_location.departure_time)
        self.assertEqual(stop_location == equal_stop_location, True)
        not_equal_stop_location = StopLocationOnTravelPath(1, 2, arrival_time=stop_location.arrival_time,
                                                       departure_time=stop_location.departure_time + timedelta(minutes=1))
        self.assertEqual(not_equal_stop_location == equal_stop_location, False)
