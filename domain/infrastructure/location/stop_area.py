from domain.infrastructure.location.stop_location import StopLocation


class StopArea(StopLocation):
    def __init__(self, longtitude, latitude, stop_locations):
        self.stop_locations = stop_locations
        super(StopArea, self).__init__(longtitude, latitude)