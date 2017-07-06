import unittest

from infrastructure.location.stop_location import StopLocation
from infrastructure.routes.route import Route
from infrastructure.routes.travel_path import TravelPath
from tests.test_route import TestRoute


class TestTravelPath(unittest.TestCase):
       def test_constructor(self):
           with self.assertRaises(ValueError) as context:
               travel_path = TravelPath(circular= False, routes= [TestRoute.GenerateTestRoute()])
           self.assertEqual(str(context.exception), "320002")