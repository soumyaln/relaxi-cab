import datetime

from app.model.location.location import Location
from app.utils.common import Rating, ServiceType


class Cab:
    def __init__(self):
        self.serviceType = None

    @property
    def service_type(self):
        return self.serviceType

    @service_type.setter
    def service_type(self, service_type):
        self.serviceType = service_type


class Driver(Cab):

    def __init__(self, name, email, phone, kycID, service_type):
        self.__name = name
        self.__email = email
        self.__kycID = kycID
        self.__phone = phone
        self.__rating = Rating.UNASSIGNED
        self.__created_at = datetime.time
        self.__available = False
        self.__serviceType = service_type
        self.__driverID = None
        self.__coordinates = Location()
        self.__trips = None

    def get_name(self):
        return self.name

    @property
    def driver_id(self):
        return self.__customerID

    @driver_id.setter
    def driver_id(self, driverID):
        self.__driverID = driverID

    @property
    def rating(self):
        return self.rating

    @rating.setter
    def rating(self, rating):
        self.rating = (self.rating + rating) // 2

    @property
    def available(self):
        return self.available

    @available.setter
    def available(self, isavailable):
        self.available = isavailable

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, longitude, latitude):
        self.__coordinates.longitude = longitude
        self.__coordinates.latitude = latitude