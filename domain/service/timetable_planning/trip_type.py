from enum import Enum


class TripType(Enum):
    # going to a deployment location
    PULLOUT = 10000
    # going to depot
    PULLIN = 10001
    # duh
    TRANSFER = 10002
    # maintenance
    DEADHEAD = 10003