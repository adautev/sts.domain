from domain.service.routes.travel_path import TravelPath
from domain.service.timetable_planning.trip_type import TripType
from domain.service.timetable_planning.vehicle_type import VehicleType


class Trip(object):
    """
    Trips represent scheduled usage of a travel path on a route for a particular day.
    TravelPath object should be with initialized arrival/departure times when Trip is initialized;
    """

    # TODO: add day types
    def __init__(self, travel_path: TravelPath, vehicle_type: VehicleType, trip_type:TripType):
        self.travel_path = travel_path
        self.vehicle_type = vehicle_type
        self.trip_type = trip_type


