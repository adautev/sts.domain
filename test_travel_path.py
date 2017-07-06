import unittest

from domain.infrastructure.location.stop_location import StopLocation
from domain.infrastructure.routes.route import Route
from domain.infrastructure.routes.travel_path import TravelPath
from domain.tests.test_route import TestRoute


class TestTravelPath(unittest.TestCase):
       def test_constructor(self):
           with self.assertRaises(ValueError) as context:
               travel_path = TravelPath(circular= False, routes= [TestRoute.GenerateTestRoute()])
           self.assertEqual(str(context.exception), "320002")