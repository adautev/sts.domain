from domain.infrastructure.location.geo_point import GeoPoint


class NetworkPoint(GeoPoint):

    def __init__(self, longtitude, latitude, name=""):
        self.name = name
        super(NetworkPoint, self).__init__(longtitude=longtitude, latitude=latitude)
