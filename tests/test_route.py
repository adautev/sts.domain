import unittest

from infrastructure.location.stop_location import StopLocation
from infrastructure.routes.route import Route



class TestRoute(unittest.TestCase):
    @staticmethod
    def GenerateTestRoute():
        return Route(name="Линия №7",
                     stop_locations=[StopLocation(1, 1, name="Орлов Мост"),
                                     StopLocation(1, 1, name="Княгиня Мария Луиза")])
    def test_constructor(self):
        route = self.GenerateTestRoute()
        self.assertEqual(len(route.stop_locations), 2)
        # verify order
        self.assertEqual(route.stop_locations[0].name, "Орлов Мост")
        self.assertEqual(route.stop_locations[1].name, "Княгиня Мария Луиза")
        self.assertEqual(route.name, "Линия №7")
