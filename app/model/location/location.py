

class Location:

    def __init__(self):
        self.longitude = None
        self.latitude = None

    @property
    def longitude(self):
        return self.longitude

    @longitude.setter
    def longitude(self, longitude):
        self.longitude = longitude

    @property
    def latitude(self):
        return self.latitude

    @latitude.setter
    def latitude(self, latitude):
        self.latitude = latitude







