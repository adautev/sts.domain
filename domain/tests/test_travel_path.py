import unittest

from domain.service.routes.travel_path import TravelPath
from domain.tests.test_route import TestRoute


class TestTravelPath(unittest.TestCase):
       def test_constructor(self):
           with self.assertRaises(ValueError) as context:
               travel_path = TravelPath(circular= False, routes= [TestRoute.GenerateTestRoute()])
           self.assertEqual(str(context.exception), "320002")