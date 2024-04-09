
class ServiceType(enumerate):
    BIKE = 1
    AUTO = 2
    CAR = 3
    SEDAN = 4
    SUV = 5


class Rating(enumerate):
    UNASSIGNED = 0
    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5


class OrderStatus(enumerate):
    CREATED = 0
    DRIVER_ASSIGNED = 1
    DRIVER_ARRIVED = 2
    PICKUP_DONE = 3
    COMPLETED = 4

