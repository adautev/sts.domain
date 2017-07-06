class ExceptionCodes(object):
    # General Rules
    # 0 - 1000 - argument validation rules
    # 1000 > - logic validation rules
    # 110000 - Geo Point
    # 120000 - Network Point
    # 130000 - Stop Point
    # 140000 - Stop Location
    # 150000 - Stop Area
    # 210000 - Network Link
    # 310000 - Route
    # 320000 - Travel Path
    # 410000 - Vehicle Working
    codes = {
        # We describe each variant of a Route as a TravelPath; the route itself combines all of the TravelPaths that
        # are used by the vehicles on the route (aggregation). The TravelPath is an ordered sequence of
        # StopLocations. As travel paths are directional, but Routes are not, each route has at least two
        # TravelPaths: one for each direction. In some very rare cases, there is only one travel path,
        # i. e. a circular route, which only runs in one direction.
        320001: "Routes cannot be less than 2 or 1 for circular travel path",
        320002: "Route count can be only one for a circular travel path"
    }
    def __init__(self): pass

