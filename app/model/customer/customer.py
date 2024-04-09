import datetime
from app.utils.common import Rating
from app.model.location.location import Location


class Customer:

    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__rating = Rating.UNASSIGNED
        self.__created_at = datetime.time
        self.__customerID = None
        self.__coordinates = Location()
        self.__trips = None

    def get_name(self):
        return self.name

    @property
    def customer_id(self):
        return self.__customerID

    @customer_id.setter
    def customer_id(self, customer_id):
        self.__customerID = customer_id

    @property
    def rating(self):
        return self.rating

    @rating.setter
    def rating(self, rating):
        self.rating = (self.rating + rating) // 2

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, longitude, latitude):
        self.__coordinates.longitude = longitude
        self.__coordinates.latitude = latitude



